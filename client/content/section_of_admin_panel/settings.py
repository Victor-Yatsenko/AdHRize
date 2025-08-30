import flet as ft

class Settings:
    def __init__(self):
        self.teams_checkbox = ft.Checkbox(label="Teams webhook",
            splash_radius=10, 
            label_position=ft.LabelPosition.LEFT,
            active_color="#000000",
            width=150,
            value=False, 
            on_change=lambda e: self.checkbox_on_change(self.teams_checkbox, self.teams_url, e)
        )
        self.teams_url = ft.TextField(label="", width=800,  disabled= True)


        self.telegram_checkbox = ft.Checkbox(label="Telegram token", 
            splash_radius=10,
            label_position=ft.LabelPosition.LEFT,
            active_color="#000000",
            width=150,
            value=False,
            on_change=lambda e: self.checkbox_on_change(self.telegram_checkbox, self.telegram_token, e)
        )
        self.telegram_token = ft.TextField(label="", width=800, disabled= True)


        self.language_text = ft.Text("Language", size=20)
        self.language_list = ft.DropdownM2(
            width=200,
            value="English",
            options=[
                ft.dropdownm2.Option("English"),
                ft.dropdownm2.Option("Українська"),
                ft.dropdownm2.Option("Русский"),
            ]
        )


    def settings(self):
        return ft.Container(
            padding=20,
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.START,
                spacing= 250,
                controls=[
                    ft.Column([
                        self.teams(),
                        self.telegram(),
                    ]
                    ),
                    ft.Column([
                        self.language()
                    ])
                ]
            )
        )


    def checkbox_on_change(self, checkbox: ft.Checkbox, fiel: ft.TextField, e: ft.ControlEvent):
        fiel.disabled = not checkbox.value
        fiel.update()


    def teams(self):
        return ft.Container(
            content=ft.Row([
                self.teams_checkbox,
                self.teams_url,
            ])
        )


    def telegram(self):
        return ft.Container(
            content=ft.Row([
                self.telegram_checkbox,
                self.telegram_token
            ])
        )
    

    def language(self):
        return ft.Container(
            content=ft.Row([
                self.language_text,
                self.language_list
            ])
        )


settings = Settings()

class Content():
    def __init__(self):
        self.content_area = ft.Container(
            expand=True,
            content=ft.Column([
                ft.Text("Это главная панель", size=25),
                ft.ElevatedButton("Кнопка на главной")
            ])
        )
        
    def change_content(self, e: ft.ControlEvent):
        index = e.control.selected_index

        if index == 0:
            content.content_area.content = ft.Column([
                ft.Text("Это главная панель", size=25),
                ft.ElevatedButton("Кнопка на главной")
            ])
        elif index == 1:
            content.content_area.content = ft.Column([
                ft.Text("Пользователи", size=25),
                ft.Switch(label="Включить кого-то")
            ])
        elif index == 2:
            content.content_area.content = ft.Column([
                settings.settings()
            ])
        self.content_area.update()

content  = Content()