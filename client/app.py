import flet as ft
from . import autorization
from .admin_panel import admin_panel
#############
def show_autorization(page: ft.Page):
    page.clean()
    # autoriz = autorization.Autorization(page, on_login=lambda: show_admin(page))
    autoriz = autorization.Autorization(page, on_login=lambda: autorization.Autorization(page))
    # autoriz = autorization.Autorization(page)
    page.add(autoriz.view)


def return_to_autorization(page: ft.Page):
    page.clean()
    autorization = admin_panel.AdminPanel(page, on_logout=lambda: show_autorization(page))
    page.add(autorization.build())
#############

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "Форма HR Новий працівник"
    page.horizontal_alignment='center'

    # auth = autorization.Autorization(page)
    # page.add(
    #     auth.view
    # )
    show_autorization(page)

ft.app(target=main, view=ft.WEB_BROWSER, port=8550)
