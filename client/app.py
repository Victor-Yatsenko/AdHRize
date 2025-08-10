import flet as ft
import json


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
    
    def on_save(e):
        data = {
            "full_name_ua": full_name_ua.value,
            "full_name_en": full_name_en.value,
            "phone":        phone.value,
            "title_ua":     title_ua.value,
            "title_en":     title_en.value,
            "department":   dept_dpd.value,
            "manager":      mgr_dpd.value
        }
        # пока просто показываем, но здесь можно отправить в API/БД/файл
        result_text.value = json.dumps(data, ensure_ascii=False, indent=2)
        page.update()
    
    # -------------------------------------------- body --------------------------------------------------------------
    title        = ft.Text("Новий працівник",               size=50, weight=ft.FontWeight.BOLD)
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
            ft.dropdownm2.Option("Варіант 3")
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
        text="Зберегти",
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
        ft.Row(controls=[form_container], 
        alignment=ft.MainAxisAlignment.CENTER))

ft.app(target=main, view=ft.WEB_BROWSER)