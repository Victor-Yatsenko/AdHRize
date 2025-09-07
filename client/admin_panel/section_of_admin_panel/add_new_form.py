import flet as ft

class AddNewForm:
    def __init__(self, page: ft.Page):
        self.page = page

        self.name_form = ft.TextField(
            border=ft.InputBorder.NONE,
            filled=True,
            # Потом сделать так hint_text=_("Форма без назви"), для перевода 
            hint_text="Форма без назви",
        )

        self.start_add_element_button = ft.TextButton(
            text="Швидкий початок із",
            icon=ft.Icons.ADD_CIRCLE
            # on_click=
        )

        self.elements = ft.SegmentedButton(
            # on_change=
            allow_multiple_selection=False,
            segments=[
                ft.Segment(
                    value="1",
                    label=ft.Text("Вибір"),
                    icon=ft.Icon(ft.Icons.CHECK_CIRCLE)
                ),
                ft.Segment(
                    value="1",
                    label=ft.Text("Вибір"),
                    icon=ft.Icon(ft.Icons.CHECK_CIRCLE)
                )
            ]
        )


        self.addNewForm = ft.Column(
            [
                self.name_form,
                self.start_add_element_button,
            ]
        )
