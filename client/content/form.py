import flet as ft


class Form:
    def __init__(self):
        self.title = ft.Text("Новий працівник",    size=50, weight=ft.FontWeight.BOLD)
        self.fields_config = [
            {"key": "full_name_ua", "label": "ПІБ (Кирилицею)"},
            {"key": "full_name_en", "label": "ПІБ (Латиницею)"},
            {"key": "phone",        "label": "Телефон"},
            {"key": "title_ua",     "label": "Посада українською"},
            {"key": "title_en",     "label": "Посада англійською"},
        ]

        self.text = {
            f["key"]: ft.TextField(label=f["label"], width=500)
            for f in self.fields_config
        }
        self.save_btn = ft.ElevatedButton(
            text="Зберегти",
            style = ft.ButtonStyle(text_style=ft.TextStyle(size=24, letter_spacing=5, weight=ft.FontWeight.BOLD),),
            width=200, height=50, color="#000000", bgcolor="#1dc054",
            on_click=self.on_save
        )

        self.dept_dpd = ft.DropdownM2(
            width=500,
            hint_text="Оберіть відділ",
            options=[
                ft.dropdownm2.Option("Варіант 1"),
                ft.dropdownm2.Option("Операційний департамент"),
                ft.dropdownm2.Option("Варіант 3"),
            ]
        )

        self.mgr_dpd = ft.DropdownM2(
            width=500,
            hint_text="Оберіть керівника",
            options=[
                ft.dropdownm2.Option("керівник 1"),
                ft.dropdownm2.Option("Управління інформаційних технологій"),
                ft.dropdownm2.Option("керівник 1")
            ]
        )

        self.result_text = ft.Text("")

        
        self.form = ft.Column(
            [
                # ft.Text("Новий працівник", size=50, weight=ft.FontWeight.BOLD),
                self.title,
                *self.text.values(),   # распаковали все поля
                # self.dept_dpd,
                # self.mgr_dpd,
                ft.Container(content=ft.Column(controls=[
                    self.section(ft.Column(controls=[ft.Text("Відділ:"), self.dept_dpd])),
                    self.section(ft.Column(controls=[ft.Text("Керівник:"), self.mgr_dpd])),
                ])),
                
                ft.Row([self.save_btn], alignment=ft.MainAxisAlignment.CENTER),
                self.result_text
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def section(self, content):
        return ft.Container(
            border=ft.border.all(2, "#0c0909"),
            border_radius=6,
            padding=10,
            content=content
        )


    def on_save(self, e, page: ft.Page):
        # пример: собрать все данные в строку
        values = {k: v.value for k, v in self.text.items()}
        self.result_text.value = f"Збережено: {values}"
        page.update()
        
f = Form()
