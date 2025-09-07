import flet as ft

class AddNewForm:
    def __init__(self, page: ft.Page):
        self.page = page
        self.text = ft.Text("test")

        self.addNewForm = ft.Column(
            [
                self.text
            ]
        )

    # def addNewForm(self):
    #     return ft.Container(
    #         content=ft.Row(
    #             controls=[
    #                 self.text
    #             ]
    #         )
    #     )