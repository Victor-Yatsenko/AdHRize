import pymsteams
from app.config import TEAMS_WEBHOOK_URL

FullName = "Іван Петренко"
FirstNameEN = "Ivan"
LastNameEN = "Petrenko"
DepartmentName = "ІТ відділ"
Title = "Розробник"
AccountPassword = "Pa$$w0rd123"


teams_message = pymsteams.connectorcard(TEAMS_WEBHOOK_URL)

message = f"""\
**✅ В AD створено нового користувача**\n
👤 **Ім'я:** {FullName} | {FirstNameEN} {LastNameEN}\n
🏢 **Відділ:** {DepartmentName}\n
💼 **Посада:** {Title}\n
🔑 **Пароль:** {AccountPassword}
"""
teams_message.text(message)
teams_message.send()