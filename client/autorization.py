import flet as ft
from server.config import CLIENT_LOGIN, CLIENT_PASSWORD, ADMIN_LOGIN, ADMIN_PASSWORD


class Autorization:
    def __init__(self, page: ft.Page, on_login = None, on_logout = None):
        self.page = page
        self.on_login = on_login
        self.on_logout = on_logout


        self.login_input    = ft.TextField(label="Введіть логін", width=300)
        self.password_input = ft.TextField(label="Введіть пароль", password=True, can_reveal_password=True, width=300)
        self.error_text     = ft.Text("", color="red", visible=False)
        self.login_btn      = ft.ElevatedButton("Увійти", on_click=self.login_click)

        self.view = ft.Column(
            [
                ft.Text("Авторизація", size=24, weight=ft.FontWeight.BOLD),
                self.login_input,
                self.password_input,
                self.error_text,
                self.login_btn
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        

    def login_click(self, e):
        if (
            self.login_input.value        == CLIENT_LOGIN
            and self.password_input.value == CLIENT_PASSWORD
        ):
            e.page.go("/form")
        elif (
            self.login_input.value        == ADMIN_LOGIN
            and self.password_input.value == ADMIN_PASSWORD
        ):
            e.page.go("/admin")
        else:
            self.error_text.value = "Логин або пароль введено невірно!"
            self.error_text.visible = True
            e.page.update()

