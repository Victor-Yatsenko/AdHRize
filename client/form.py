import flet as ft
import requests

class Form:
    def __init__(self):
        self.title = ft.Text("New employee",    size=50, weight=ft.FontWeight.BOLD)
        self.fields_config = [
            {"key": "full_name_UA", "label": "ПІБ (Кирилицею)"},
            {"key": "full_name_EN", "label": "ПІБ (Латиницею)"},
            {"key": "phone",        "label": "Телефон"},
            {"key": "title_UA",     "label": "Посада українською"},
            {"key": "title_EN",     "label": "Посада англійською"},
        ]
        # self.inputs = {}

        self.text = {
            f["key"]: ft.TextField(label=f["label"], width=500)
            for f in self.fields_config
        }
        self.save_btn = ft.ElevatedButton(
            text="Save",
            style = ft.ButtonStyle(text_style=ft.TextStyle(size=24, letter_spacing=5, weight=ft.FontWeight.BOLD),),
            width=200, height=50, color="#000000", bgcolor="#1dc054",
            on_click=self.on_save
        )

        self.dept_dpd = ft.DropdownM2(
            width=500,
            hint_text="Select a department",
            options=[
                ft.dropdownm2.Option("Варіант 1"),
                ft.dropdownm2.Option("Операційний департамент"),
                ft.dropdownm2.Option("Варіант 3"),
            ]
        )

        self.mgr_dpd = ft.DropdownM2(
            width=500,
            hint_text="Select a manager",
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
                    self.section(ft.Column(controls=[ft.Text("Department:"), self.dept_dpd])),
                    self.section(ft.Column(controls=[ft.Text("Manager:"), self.mgr_dpd])),
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
    

    def on_save(self, e):
        # пример: собрать все данные в строку
        values = {k: v.value for k, v in self.text.items()}
        self.result_text.value = f"Збережено: {values}"
        # page.update()
        e.page.update()
    # def on_save(self, e):
    #     data = {
    #         "FullNameUA":       self.text["full_name_UA"].value,
    #         "FullNameEN":       self.text["full_name_EN"].value,
    #         "Phone":            self.text["phone"]       .value,
    #         "Title":            f"{self.text["title_EN"] .value} | {self.text["title_UA"].value}",
    #         "DepartmentName":   self.dept_dpd            .value,
    #         "ManagerName":      self.mgr_dpd             .value
    #     }
    #     # self.result_text.value = f"Збережено: {data}"
    #     # page.update()
    #     response = requests.post("http://", json=data)
    #     # page.update()
    #     e.page.update()
    #     return response

f = Form()
