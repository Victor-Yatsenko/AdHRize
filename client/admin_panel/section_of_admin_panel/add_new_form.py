import flet as ft


class AddNewForm:
    def __init__(self, page: ft.Page):
        self.page = page

        self.back_button = ft.Container(
            ft.ElevatedButton(
                content=ft.Row(
                    controls=[
                        ft.Icon(name=ft.Icons.ARROW_BACK, color=ft.Colors.WHITE, size=30),
                        ft.Text("Back", size=20),
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
            hint_text="Form without a name",
        )

        self.start_add_element_button = ft.TextButton(
            text="Add element",
            icon=ft.Icons.ADD_CIRCLE,
            on_click=self.toggle_elements
            
        )
        self.elements = ft.SegmentedButton(
            visible=False,
            selected=[],
            on_change=self.change_add_elements,
            allow_empty_selection=True,
            segments=[
                ft.Segment(
                    value="1",
                    label=ft.Text("Select"),
                    icon=ft.Icon(ft.Icons.CHECK_CIRCLE)
                ),
                ft.Segment(
                    # value=self.add_elements(index=0),
                    value="2",
                    label=ft.Text("Text"),
                    icon=ft.Icon(ft.Icons.TEXT_FIELDS),
                    
                ),
                ft.Segment(
                    value="3",
                    label=ft.Text("Date"),
                    icon=ft.Icon(ft.Icons.CALENDAR_MONTH)
                ),
            ],
        )
   
        self.add_new_form = ft.Container(
            ft.Column(
                [
                    self.back_button,
                    self.name_form,
                    self.start_add_element_button,
                    self.elements
                ]
            )
        )


    def back_to_main_section(self, e: ft.ControlEvent):
        e.page.go("/admin")



    def toggle_elements(self, e):
        self.elements.visible = not self.elements.visible 
        self.elements.update()


    def change_add_elements(self, e):
        print("on_change data : " + str(e.data))


    # def add_elements(self, index):
    #     if index == 0:
    #         x = ft.Container(
    #             content=ft.Column(
    #                 controls=[
    #                     ft.TextField(
    #                         value="Питання"
    #                     ),
    #                     ft.TextField(
    #                         value="Напишіть відповідь"
    #                     )
    #                 ]
    #             )
    #         )
    #         return self.page.add(x)
            # return ft.Container(
            #     content=[
            #         ft.TextField(
            #             value="Питання"
            #         ),
            #         ft.TextField(
            #             value="Напишіть відповідь"
            #         )
            #     ]
            # )
        # self.text_question = ft.TextField(
        #     value="Питання"
        # )
        # self.text_ansver = ft.TextField(
        #     value="Напишіть відповідь"
        # )

