import flet as ft
from .admin_panel import admin_panel
from client import form
from server.config import CLIENT_LOGIN, CLIENT_PASSWORD, ADMIN_LOGIN, ADMIN_PASSWORD


class Autorization:
    def __init__(self, page: ft.Page):
        self.page = page

        # self.CLIENT_LOGIN = "u"
        # self.CLIENT_PASSWORD = "1"

        # self.ADMIN_LOGIN = "a"
        # self.ADMIN_PASSWORD = "1"

        self.login_input    = ft.TextField(label="Введіть логін", width=300)
        self.password_input = ft.TextField(label="Введіть пароль", password=True, can_reveal_password=True, width=300)
        self.error_text     = ft.Text("", color="red", visible=False)
        self.login_btn = ft.ElevatedButton("Увійти", on_click=self.login_click)

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
            self.page.clean()
            self.page.add(ft.Row(controls=[form.f.form], alignment=ft.MainAxisAlignment.CENTER))
        elif (
            self.login_input.value        == ADMIN_LOGIN
            and self.password_input.value == ADMIN_PASSWORD
        ):
            self.page.clean()
            self.page.add(ft.Row(expand=True, controls=[admin_panel.a.build()], alignment=ft.MainAxisAlignment.START))
        else:
            self.error_text.value = "Логин або пароль введено невірно!"
            self.error_text.visible = True
            self.page.update()

