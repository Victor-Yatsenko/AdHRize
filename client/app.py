import flet as ft
from client import route

#############

# def show_autorization(page: ft.Page):
#     page.clean()
#     autoriz = autorization.Autorization(page, r=page)
#     page.add(autoriz.view)

#############


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "ADHRize"
    page.horizontal_alignment='center'


    page.on_route_change = route.route_change
    page.go(page.route)


ft.app(target=main, view=ft.WEB_BROWSER, port=8550)
