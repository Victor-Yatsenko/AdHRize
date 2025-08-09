import flet as ft

def main(page: ft.Page):
    page.title = "AdHRize HR Form"
    page.add(ft.Text("Привет! Здесь форма для HR."))

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)
