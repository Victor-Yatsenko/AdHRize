import flet as ft

from client.content import autorization


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "Форма HR Новий працівник"
    page.horizontal_alignment='center'

    auth = autorization.Autorization(page)
    page.add(
        auth.view
    )

ft.app(target=main, view=ft.WEB_BROWSER, port=8550)
