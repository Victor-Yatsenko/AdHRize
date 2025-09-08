import flet as ft
from .section_of_admin_panel import settings
from client.admin_panel.section_of_admin_panel import main_section
from .. import autorization

class AdminPanel:
    def __init__(self, page: ft.Page, on_login = None):
        self.page = page
        self.on_login = on_login

    def build(self, side_bar: "SideBar", content: "Content"):
        return ft.Row(
            expand=True,
            controls=[
                side_bar.side_bar(content),
                content.content_area
            ]
        )

class SideBar(ft.NavigationRail):
    def __init__(self, ):
        super().__init__()

    def side_bar(self, content: "Content"):
        return ft.Container(
            border_radius = 15,
            content = ft.NavigationRail(
                bgcolor = "#000000",
                selected_index = 0,
                label_type = ft.NavigationRailLabelType.ALL,
                min_width = 100,
                min_extended_width = 400,
                group_alignment = -1.0,
                destinations = [
                    ft.NavigationRailDestination(
                        icon          = ft.Icon(ft.Icons.DASHBOARD_OUTLINED, color = "#eaeaea"),
                        selected_icon = ft.Icon(ft.Icons.DASHBOARD,          color = "#000000"),
                        label_content = ft.Text("Головна",                   color = "#eaeaea"),
                    ),
                    ft.NavigationRailDestination(
                        icon          = ft.Icon(ft.Icons.PEOPLE_OUTLINE,     color = "#eaeaea"),
                        selected_icon = ft.Icon(ft.Icons.PEOPLE,             color = "#000000"),
                        label_content = ft.Text("Користувачі",               color = "#eaeaea"),
                    ),
                    ft.NavigationRailDestination(
                        icon          = ft.Icon(ft.Icons.SETTINGS_OUTLINED,  color = "#eaeaea"),
                        selected_icon = ft.Icon(ft.Icons.SETTINGS,           color = "#000000"),
                        label_content = ft.Text("Налаштування",              color = "#eaeaea"),
                    ),
                    ft.NavigationRailDestination(
                        icon          = ft.Icon(ft.Icons.EXIT_TO_APP,        color = "#eaeaea"),
                        label_content = ft.Text("Вихід",                     color = "#eaeaea"),
                    ),
                ],
                on_change = content.change_content
            ),
        )
    
class Content:
    def __init__(self, page: ft.Page, on_login = None):
        self.page = page
        self.on_login = on_login
        self.content_area = ft.Container(
            expand=True,
            content=ft.Column([
                main_section.main_section.main_section

            ])
        )

    def change_content(self, e: ft.ControlEvent):
        index = e.control.selected_index

        if index == 0:
            self.content_area.content = ft.Column([
                main_section.main_section.main_section
            ])
        elif index == 1:
            self.content_area.content = ft.Column([
                ft.Text("Пользователи", size=25),
                ft.Switch(label="Включить кого-то")
            ])
        elif index == 2:
            self.content_area.content = ft.Column([
                settings.settings.settings()
            ])
        elif index == 3:
            panel = autorization.Autorization(self.page, self.on_login)
            e.page.clean()
            e.page.add(panel.view)
            return

        self.content_area.update()
