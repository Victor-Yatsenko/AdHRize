import flet as ft
import requests
from server.config import CLIENT_LOGIN, CLIENT_PASSWORD


def section(content):
    return ft.Container(
        border=ft.border.all(2, "#0c0909"),
        border_radius=6,
        padding=10,
        content=content
    )


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "Форма HR Новий працівник"
    page.horizontal_alignment='center'

    # --------------------------------------- Авторизація ---------------------------------------------------------
    login_input    = ft.TextField(label="Введіть логін", width=300)
    password_input = ft.TextField(label="Введіть пароль", password=True, can_reveal_password=True, width=300)
    error_text     = ft.Text("", color="red", visible=False)

    def login_click(e):
        if login_input.value == CLIENT_LOGIN and password_input.value == CLIENT_PASSWORD:
            page.clean()
            page.add(ft.Row(controls=[form_container], alignment=ft.MainAxisAlignment.CENTER))
        else:
            error_text.value = "Логин або пароль введено невірно!"
            error_text.visible = True
            page.update()

    login_btn = ft.ElevatedButton("Увійти", on_click=login_click)
    # ---------------------------------------------------------------------------------------------------------------
    
    def on_save(e):
        data = {
            "FullNameUA":       full_name_ua.value,
            "FullNameEN":       full_name_en.value,
            "Phone":            phone.value,
            "Title":            f"{title_en.value} | {title_ua.value}",
            "DepartmentName":   dept_dpd.value,
            "ManagerName":      mgr_dpd.value
        }

        response = requests.post("http://127.0.0.1:8081/save", json=data)
        page.update()
        return response
    
    # -------------------------------------------- body --------------------------------------------------------------
    title        = ft.Text(           "Новий працівник",    size=50, weight=ft.FontWeight.BOLD)
    full_name_ua = ft.TextField(label="ПІБ (Кирилицею)",    width=500)
    full_name_en = ft.TextField(label="ПІБ (Латиницею)",    width=500)
    phone        = ft.TextField(label="Телефон",            width=500)
    title_ua     = ft.TextField(label="Посада українською", width=500)
    title_en     = ft.TextField(label="Посада англійською", width=500)

    dept_dpd = ft.DropdownM2(
        width=500,
        hint_text="Оберіть відділ",
        options=[
            ft.dropdownm2.Option("Варіант 1"),
            ft.dropdownm2.Option("Операційний департамент"),
            ft.dropdownm2.Option("Варіант 3"),
        ]
    )
    
    mgr_dpd = ft.DropdownM2(
        width=500,
        hint_text="Оберіть керівника",
        options=[
            ft.dropdownm2.Option("керівник 1"),
            ft.dropdownm2.Option("Управління інформаційних технологій"),
            ft.dropdownm2.Option("керівник 1")
        ]
    )

    save_btn = ft.ElevatedButton(
        text="Створити",
        style = ft.ButtonStyle(text_style=ft.TextStyle(size=24, letter_spacing=5, weight=ft.FontWeight.BOLD),),
        width=200, height=50, on_click=on_save, color="#000000", bgcolor="#1dc054")

    result_text = ft.Text()
    # ----------------------------------------------------------------------------------------------------------------

    form_container = ft.Container(
        width=520,
        padding=ft.padding.all(12),
        content=ft.Column(
            controls=[
                ft.Container(content=ft.Column(controls=[
                    title, full_name_ua, full_name_en, phone, title_ua, title_en
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,)),

                ft.Container(content=ft.Column(controls=[
                    section(ft.Column(controls=[ft.Text("Відділ:"), dept_dpd])),
                    section(ft.Column(controls=[ft.Text("Керівник:"), mgr_dpd])),
                ])),

                ft.Row(controls=[save_btn], alignment=ft.MainAxisAlignment.CENTER),
                result_text
            ]
        )
    )

    page.add(
        ft.Column(
            [
                ft.Text("Авторизація", size=24, weight=ft.FontWeight.BOLD),
                login_input,
                password_input,
                error_text,
                login_btn
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ))

ft.app(target=main, view=ft.WEB_BROWSER, port=8550)