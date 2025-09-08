import flet as ft


class AddNewForm:
    def __init__(self, page: ft.Page):
        self.page = page

        self.back_button = ft.Container(
            ft.ElevatedButton(
                content=ft.Row(
                    controls=[
                        ft.Icon(name=ft.Icons.ARROW_BACK, color=ft.Colors.WHITE, size=30),
                        ft.Text("Назад", size=20),
                    ],
                    alignment=ft.MainAxisAlignment.START
                ),
                style = ft.ButtonStyle(text_style=ft.TextStyle(size=24,)),
                color="#FFFFFF", bgcolor="#000000", height=50, width= 120,
                on_click=self.back_to_main_section
            ),
        )
        
        
        self.name_form = ft.TextField(
            border=ft.InputBorder.NONE,
            filled=True,
            # Потом сделать так hint_text=_("Форма без назви"), для перевода 
            hint_text="Форма без назви",
        )

        self.start_add_element_button = ft.TextButton(
            text="Додати елемент",
            icon=ft.Icons.ADD_CIRCLE,
            on_click=self.toggle_elements
            
        )

        self.elements = ft.SegmentedButton(
            visible=False,
            selected=[],
            on_change=self.handle_change,
            allow_empty_selection=True,
            segments=[
                ft.Segment(
                    value="1",
                    label=ft.Text("Вибір"),
                    icon=ft.Icon(ft.Icons.CHECK_CIRCLE)
                ),
                ft.Segment(
                    value="2",
                    label=ft.Text("Текст"),
                    icon=ft.Icon(ft.Icons.TEXT_FIELDS)
                ),
                ft.Segment(
                    value="3",
                    label=ft.Text("Дата"),
                    icon=ft.Icon(ft.Icons.CALENDAR_MONTH)
                ),
            ],
        )
   
        self.add_new_form = ft.Column(
            [
                self.back_button,
                self.name_form,
                self.start_add_element_button,
                self.elements
            ]
        )

    def handle_change(self, e):
        print("on_change data : " + str(e.data))


    def toggle_elements(self, e):
        self.elements.visible = not self.elements.visible 
        self.elements.update()


    def back_to_main_section(self, e: ft.ControlEvent):
        e.page.clean()
        from client.admin_panel.admin_panel import AdminPanel, SideBar, Content
        viev = AdminPanel(e)
        e.page.add(viev.build(side_bar=SideBar(), content=Content(e)))