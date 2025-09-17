import flet as ft
from locales import switch_localization as sl


class Settings:
    def __init__(self, side_bar = None, page = ft.Page):
        self.page = page
        self.side_bar = side_bar
        self.teams_checkbox = ft.Checkbox(label=ft.Text(sl._("Teams webhook")),
            splash_radius=10, 
            label_position=ft.LabelPosition.LEFT,
            active_color="#000000",
            width=150,
            value=False, 
            on_change=lambda e: self.checkbox_on_change(self.teams_checkbox, self.teams_url, e)
        )
        self.teams_url = ft.TextField(label="", width=800,  disabled= True)

        self.telegram_checkbox = ft.Checkbox(label=ft.Text(sl._("Telegram token")), 
            splash_radius=10,
            label_position=ft.LabelPosition.LEFT,
            active_color="#000000",
            width=150,
            value=False,
            on_change=lambda e: self.checkbox_on_change(self.telegram_checkbox, self.telegram_token, e)
        )
        self.telegram_token = ft.TextField(label="", width=800, disabled= True)

        self.language_text = ft.Text((sl._("Language")), size=20)
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
                sl.set_language("en")
            
            case "Українська":
                sl.set_language("ua")

            case "Русский":
                sl.set_language("ru")

        self.language_text.value = sl._("Language")
        self.teams_checkbox.label = sl._("Teams webhook")
        self.telegram_checkbox.label = sl._("Telegram token")

        
        e.page.update()



        # e.page.clean()
        # e.page.add(Settings().settings())
        
        
        # e.page.update()

        # side_bar = admin_panel.AdminPanel(e.page)
        # from client.admin_panel.admin_panel import SideBar

        # self.side_bar.content.controls[0].on_change = new_content.change_content
        

        # e.page.clean()
        # e.page.add(
        #     ft.Row([
        #         self.side_bar.get_control(),
        #         new_settings
        #     ])
        # )


        # e.page.clean()
        # e.page.add(
        #     ft.Row([
        #         self.side_bar,
        #         Settings(self.side_bar).settings()
        #     ])
        # )
            # Settings().settings())
        # e.page.add(Settings(side_bar).settings())
        # self.language_text.value = switch_localization._("Language")
        # e.page.on_route_change = settings
        
        # e.page.update()

        



        # main_row = None
        # for ctrl in e.page.controls:
        #     if isinstance(ctrl, ft.Row) and len(ctrl.controls) >= 2:
        #         left = ctrl.controls[0]
        #         # left должен быть Container с NavigationRail в left.content
        #         if hasattr(left, "content") and isinstance(left.content, ft.NavigationRail):
        #             main_row = ctrl
        #             break

        # # 3) если не нашли — делаем безопасный fallback: пересоздаём админский layout
        # if main_row is None:
        #     from client.admin_panel.admin_panel import AdminPanel, SideBar, Content
        #     side_bar = SideBar()
        #     content = Content(e.page)
        #     e.page.clean()
        #     e.page.add(ft.Row(expand=True, controls=[side_bar.side_bar(content), content.content_area]))
        #     # теперь найдём добавленный Row
        #     for ctrl in e.page.controls:
        #         if isinstance(ctrl, ft.Row) and len(ctrl.controls) >= 2:
        #             main_row = ctrl
        #             break
        #     if main_row is None:
        #         # если и теперь ничего — просто обновляем страницу и выходим
        #         e.page.update()
        #         return

        # # 4) обновляем правую колонку (контент)
        # left_container = main_row.controls[0]   # это Container с NavigationRail
        # right_container = main_row.controls[1]  # это Container (content_area)

        # # создаём новый Settings, передаём левый контейнер как side_bar
        # new_settings_control = Settings(side_bar=left_container).settings()
        # # new_settings = Settings(side_bar=self.side_bar, page=e.page).settings()

        # # помещаем новый контент внутрь правой колонки; оборачиваем в Column, т.к. раньше там Column
        # right_container.content = ft.Column([new_settings_control])
        # e.page.update()

    
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


# settings = Settings()