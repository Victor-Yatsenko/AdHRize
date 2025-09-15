import gettext
import os
from client.admin_panel.section_of_admin_panel.settings import Settings






# LOCALE_DIR = "locales"
# LANG = "en"
sett = Settings.dropdown_changed
LANG = str(sett)

# Загружаем перевод (messages.mo внутри locales/<lang>/LC_MESSAGES/)
t = gettext.translation(
    "messages", 
    localedir="locales",
    languages=[LANG], 
    fallback=True  # если нет перевода - вернет оригинал
)

t.install()
_ = t.gettext   # сокращение
