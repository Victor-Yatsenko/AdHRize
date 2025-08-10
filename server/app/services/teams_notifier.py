import pymsteams, os
from dotenv import load_dotenv


FullName = "Іван Петренко"
FirstNameEN = "Ivan"
LastNameEN = "Petrenko"
DepartmentName = "ІТ відділ"
Title = "Розробник"
AccountPassword = "Pa$$w0rd123"


load_dotenv()
teams_webhook_url = os.getenv("TEAMS_WEBHOOK_URL")
teams_message = pymsteams.connectorcard(teams_webhook_url)

message = f"""\
**✅ В AD створено нового користувача**\n
👤 **Ім'я:** {FullName} | {FirstNameEN} {LastNameEN}\n
🏢 **Відділ:** {DepartmentName}\n
💼 **Посада:** {Title}\n
🔑 **Пароль:** {AccountPassword}
"""
teams_message.text(message)
teams_message.send()