# Параметри АД
#################################################################
param (
    # Account
    [string] $FirstNameUA,
    [string] $LastNameUA,
    [string] $FirstNameEN,
    [string] $LastNameEN,
    [string] $UserUPNlogon,

    # Organization
    [string] $Office,
    [string] $Email,
    [string] $WebPage,
    [string] $Phone,
    [string] $Title,
    [string] $DepartmentName,
    [string] $Company,
    [string] $ManagerName,
    [string] $Description
)
# Account
$SamAccountName = "${FirstNameEN}.${LastNameEN}"
$FullName = "${LastNameUA} ${FirstNameUA}"
$DisplayName = "${FullName} / ${FirstNameEN} ${LastNameEN}"

# Генеруємо пароль
. "$PSScriptRoot\PasswordGenerator.ps1"
$pg = [PasswordGenerator]::new()
$pg.Length = 10 # Довжина паролю
$pg.UseSymbols = $true
$AccountPassword = $pg.Generate()
#################################################################

# Підготовка файлів конфігурації
# Шлях до JSON-файлів
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$SettingsJson = Join-Path $ScriptDir "settings"                   # Папки з файлами
$StructureJsonPath = Join-Path $SettingsJson "ad_structure.json"  # Структура ад
$ManagersJsonPath = Join-Path $SettingsJson "managers.json"       # Структура керівників
$GroupsJsonPath = Join-Path $SettingsJson "groups.json"           # Групові політики

# Завантажуємо структури з JSON
$StructureAD = Get-Content $StructureJsonPath -Raw | ConvertFrom-Json
$StructureManagers = Get-Content $ManagersJsonPath -Raw | ConvertFrom-Json
$StructureGroups = Get-Content $GroupsJsonPath -Raw | ConvertFrom-Json


# Пошук потрібного dn структури AD
function Get-DnByName {
    param (
        [string] $Name,
        $StructureJson
    )

    foreach ($dept in $StructureJson.PSObject.Properties) {
        if ($dept.Name -eq $Name) {
            return $dept.Value.dn
        }

        if ($dept.Value.subdepartments) {
            $result = Get-DnByName -Name $Name -StructureJson $dept.Value.subdepartments
            if ($result) {
                return $result
            }
        }
    }

    return $null
}

# Пошук відділу
$OUPath = Get-DnByName -Name $DepartmentName -StructureJson $StructureAD
if (-not $OUPath) {
    Write-Host "Відділ або підвідділ '$DepartmentName' не знайдено в структурі!"
    exit 1
}

# Пошук керівника
$Manager = Get-DnByName -Name $ManagerName -StructureJson $StructureManagers
if (-not $Manager) {
    Write-Host "Керівника '$ManagerName' не знайдено в структурі!"
    exit 1
}

# створюємо користувача та заповнюємо всі потрібні поля
try {
    New-ADUser `
        -GivenName $FirstNameUA `
        -Surname $LastNameUA `
        -Name $FullName `
        -UserPrincipalName $UserUPNlogon `
        -SamAccountName $SamAccountName `
        -DisplayName $DisplayName `
        -Office $Office `
        -EmailAddress $Email `
        -OfficePhone $Phone `
        -Title $Title `
        -Department	$DepartmentName `
        -Company $Company `
        -Manager $Manager `
        -Description $Description `
        -Path $OUPath `
        -AccountPassword (ConvertTo-SecureString $AccountPassword -AsPlainText -Force) `
        -Enabled $true

    Set-ADUser -Identity $SamAccountName -Replace @{wWWHomePage = $WebPage}
    Write-Host "Користувача $FullName успішно створено в OU: $DepartmentName `nКористувачу надано пароль: $AccountPassword `n"
}
catch {
    Write-Host "Помилка при створенні користувача: $_"
}


# Додаємо групові політики
#############################################################################################
$GroupInfo = ($StructureGroups.PSObject.Properties |
    Where-Object { $_.Name.Trim() -eq $Title.Trim() }).Value

if (-not $GroupInfo) {
    Write-Host "Групи для посади '$Title' не знайдено в структурі!"
    exit 1
}

$Groups = @()
$Groups += $StructureGroups.default
$Groups += $GroupInfo
$Groups = $Groups | Sort-Object -Unique

foreach ($Group in $Groups) {
    try {
        # Перевіряємо чи існує політика
        if (Get-ADGroup -Identity $Group -ErrorAction Stop) {
            Add-ADGroupMember -Identity $Group -Members $SamAccountName -ErrorAction Stop
            Write-Host "Користувачу назначено групову політику:  $Group"
        }
    } catch {
        Write-Host "Помилка при додаванні групової політики '$Group': $_"
    }
}
Write-Host ""
#############################################################################################


# Відправка повідомлень в Тeams
######################################################################################################
# Пошук токену
$envLines = Get-Content ".env"
foreach ($line in $envLines) {
    if ($line -match "^\s*TEAMS_WEBHOOK_URL\s*=\s*(.+)$") {
        $WebhookURL = $matches[1].Trim()
        break
    }
}
if (-not $WebhookURL) {
    Write-Error "Змінну TEAMS_WEBHOOK_URL не знайдено в .env"
    exit
}

# Повідомлення для Teams
$message = @"
**✅ В AD створено нового користувача** `n
👤 **Ім'я:** $FullName | $FirstNameEN $LastNameEN`n
🏢 **Відділ:** $DepartmentName `n
💼 **Посада:** $Title `n
🔑 **Пароль:** $AccountPassword
"@

# Формуємо JSON payload (перекодуємо з UTF-16LE в UTF-8)
$payload = @{ text = $message } | ConvertTo-Json -Depth 2
$utf8Bytes = [System.Text.Encoding]::UTF8.GetBytes($payload)
$utf8Body = [System.IO.MemoryStream]::new($utf8Bytes)

# Відправляємо повідомлення в Teams
Write-Host "TEAMS_WEBHOOK_URL: $WebhookURL"

Invoke-RestMethod -Method Post -Uri $WebhookURL -Body $utf8Body -ContentType 'application/json'
######################################################################################################