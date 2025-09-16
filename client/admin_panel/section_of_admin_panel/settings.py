import flet as ft
from locales import switch_localization
from client.admin_panel import admin_panel

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

        self.telegram_checkbox = ft.Checkbox(label=("Telegram token"), 
            splash_radius=10,
            label_position=ft.LabelPosition.LEFT,
            active_color="#000000",
            width=150,
            value=False,
            on_change=lambda e: self.checkbox_on_change(self.telegram_checkbox, self.telegram_token, e)
        )
        self.telegram_token = ft.TextField(label="", width=800, disabled= True)


        self.language_text = ft.Text((switch_localization._("Language")), size=20)
        self.language_list = ft.Dropdown(
            width=200,
            value = "English",
            on_change = self.dropdown_changed,
            options=[
                ft.dropdown.Option(key = "English"),
                ft.dropdown.Option(key = "Українська"),
                ft.dropdown.Option(key = "Русский"),
            ],
            
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

    def dropdown_changed(self, e):
        # language = self.language_list.key
        value = e.control.value

        match value:
            case "English":
                switch_localization.set_language("en")
            
            case "Українська":
                switch_localization.set_language("ua")

            case "Русский":
                switch_localization.set_language("ru")

        # self.language_text.value = switch_localization._("Language")
        e.page.on_route_change = settings
        
        e.page.update()

    
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