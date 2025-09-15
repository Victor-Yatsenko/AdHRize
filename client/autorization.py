import flet as ft
from server.config import CLIENT_LOGIN, CLIENT_PASSWORD, ADMIN_LOGIN, ADMIN_PASSWORD
from locales import switch_localization


class Autorization:
    def __init__(self, page: ft.Page, on_login = None, on_logout = None):
        self.page      = page
        self.on_login  = on_login
        self.on_logout = on_logout

        self.login_input    = ft.TextField(label=("Enter your login"), width=300)
        self.password_input = ft.TextField(label="Enter password", password=True, can_reveal_password=True, width=300)
        self.error_text     = ft.Text("Incorrect login or password!", color="red", visible=False)
        self.login_btn      = ft.ElevatedButton("Log in", on_click=self.login_click)

        self.view = ft.Column(
            [
                ft.Text(switch_localization._("Authorization"), size=24, weight=ft.FontWeight.BOLD),
                self.login_input,
                self.password_input,
                self.error_text,
                self.login_btn
            ],
            alignment            = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER
        )
        

    def login_click(self, e):
        self.CLIENT_LOGIN    = CLIENT_LOGIN
        self.CLIENT_PASSWORD = CLIENT_PASSWORD
        self.ADMIN_LOGIN     = ADMIN_LOGIN
        self.ADMIN_PASSWORD  = ADMIN_PASSWORD

        login                = self.login_input.value
        password             = self.password_input.value

        match (login, password):
            case self.CLIENT_LOGIN, self.CLIENT_PASSWORD:
                e.page.go("/form")

            case (self.ADMIN_LOGIN, self.ADMIN_PASSWORD):
                e.page.go("/admin")

            case _:
                self.error_text.visible = True
                e.page.update()