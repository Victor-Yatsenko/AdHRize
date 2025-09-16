import gettext
import os
# from client.admin_panel.section_of_admin_panel.settings import Settings


LOCALE_DIR = os.path.dirname(__file__)
DOMAIN = "messages"

_current_lang = "en"
_t = gettext.translation(DOMAIN, localedir=LOCALE_DIR, languages=[_current_lang], fallback=True)
_t.install()
_ = _t.gettext

def set_language(lang: str):
    global _t, _, _current_lang
    _current_lang = lang
    _t = gettext.translation(DOMAIN, localedir=LOCALE_DIR, languages=[lang], fallback=True)
    _t.install()
    _ = _t.gettext

def get_language():
    return _current_lang



# # LOCALE_DIR = "locales"
# # LANG = "ua"
# # sett = Settings().dropdown_changed
# # lang = str(sett)
# lang = "ua"

# # Загружаем перевод (messages.mo внутри locales/<lang>/LC_MESSAGES/)
# t = gettext.translation(
#     "messages", 
#     localedir="locales",
#     languages=[lang], 
#     fallback=True  # если нет перевода - вернет оригинал
# )

# t.install()
# _ = t.gettext   # сокращение
