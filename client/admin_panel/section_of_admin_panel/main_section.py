import flet as ft
from client.admin_panel.section_of_admin_panel.add_new_form import AddNewForm


class MainSection:
    def __init__(self):
        self.add_new_form = ft.Container(
            ft.ElevatedButton(
                content=ft.Row(
                    controls=[
                        ft.Icon(name=ft.Icons.ASSIGNMENT_ADD, color=ft.Colors.WHITE, size=30),
                        ft.Text("Add  new  form", size=20),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                style = ft.ButtonStyle(text_style=ft.TextStyle(size=24,)),
                color="#FFFFFF", bgcolor="#000000", height=50, width= 220,
                on_click=self.click_add_new_form_button
            ),
        )
        self.field_search_form = ft.TextField(label="Пошук", width=500)


    def click_add_new_form_button(self, e: ft.ControlEvent):
        e.page.clean()
        viev = AddNewForm(e.page)
        e.page.add(viev.addNewForm)


    def main_section(self):
        return ft.Container(
            padding=20,
            content=ft.Row(
                # vertical_alignment=ft.CrossAxisAlignment.START,
                spacing= 250,
                controls=[
                    ft.Column([
                        self.add_new_form
                    ],),
                    
                    ft.Column([
                        self.field_search_form
                    ],)
                ]
            )
        )
    
    # пошук форми
    def search_form(self):
        self.field_search_form.value



main_section = MainSection()