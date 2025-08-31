import flet as ft
from .section_of_admin_panel import settings
from .. import autorization

class AdminPanel:
    def __init__(self, page: ft.Page, on_logout):
        self.page = page
        self.on_logout = on_logout

    def build(self):
        return ft.Row(
            controls=[
                side_bar.side_bar(),
                # settings.content.content_area
                # Content.content_area
                content.content_area
                
            ]
        )

class SideBar(ft.NavigationRail):
    def __init__(self):
        super().__init__()
        # self.page = page

    def side_bar(self):
        return ft.Container(
            border_radius = 15,
            content = ft.NavigationRail(
                bgcolor = "#000000",
                selected_index = 0,
                label_type = ft.NavigationRailLabelType.ALL,
                min_width = 100,
                min_extended_width = 400,
                # indicator_color = "#ffffffff",
                # group_alignment = 0.0,#0.5
                group_alignment = -1.0,
                destinations = [
                    ft.NavigationRailDestination(
                        icon          = ft.Icon(ft.Icons.DASHBOARD_OUTLINED, color = "#eaeaea"),
                        selected_icon = ft.Icon(ft.Icons.DASHBOARD,          color = "#000000"),
                        label_content = ft.Text("Головна",                   color = "#eaeaea"),
                        # on_change     = content.change_content
                    ),
                    ft.NavigationRailDestination(
                        icon          = ft.Icon(ft.Icons.PEOPLE_OUTLINE,     color = "#eaeaea"),
                        selected_icon = ft.Icon(ft.Icons.PEOPLE,             color = "#000000"),
                        label_content = ft.Text("Користувачі",               color = "#eaeaea"),
                        # on_change     = content.change_content
                    ),
                    ft.NavigationRailDestination(
                        icon          = ft.Icon(ft.Icons.SETTINGS_OUTLINED,  color = "#eaeaea"),
                        selected_icon = ft.Icon(ft.Icons.SETTINGS,           color = "#000000"),
                        label_content = ft.Text("Налаштування",              color = "#eaeaea"),
                        # on_change     = content.change_content
                    ),
                    ft.NavigationRailDestination(
                        icon          = ft.Icon(ft.Icons.EXIT_TO_APP,        color = "#eaeaea"),
                        selected_icon = ft.Icon(ft.Icons.EXIT_TO_APP,        color = "#000000"),
                        label_content = ft.Text("Вихід",                     color = "#eaeaea"),
                        # on_change     = content.content_area.on_click=
                        
                    )
                ],
                on_change = content.change_content
                # on_change = lambda e: content.change_content(e, self.page)
                # on_change = settings.content.change_content
            ),
        )
    
class Content():
    def __init__(self):
        # self.on_logout = on_logout
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
                settings.settings.settings()
            ])
        # elif index == 3:
        #     content.content_area.content = self.on_logout
        # elif index == 3:
        #     self.page.clean()
        #     self.page.add(ft.Row(
        #         controls=[autorization.Autorization(self.page)],
        #         alignment=ft.MainAxisAlignment.CENTER
        #     ))
            # page.add(ft.Row(controls=[form.f.form], alignment=ft.MainAxisAlignment.CENTER))
            # page.add(ft.Row(controls=[autorization.Autorization(page)], alignment=ft.MainAxisAlignment.CENTER))

        self.content_area.update()



# class Content():
#     def __init__(self):
#         self.content_area = ft.Container(
#             expand=True,
#             content=ft.Column([
#                 ft.Text("Это главная панель", size=25),
#                 ft.ElevatedButton("Кнопка на главной")
#             ])
#         )
        
#     def change_content(self, e: ft.ControlEvent):
#         index = e.control.selected_index

#         if index == 0:
#             content.content_area.content = ft.Column([
#                 ft.Text("Это главная панель", size=25),
#                 ft.ElevatedButton("Кнопка на главной")
#             ])
#         elif index == 1:
#             content.content_area.content = ft.Column([
#                 ft.Text("Пользователи", size=25),
#                 ft.Switch(label="Включить кого-то")
#             ])
#         elif index == 2:
#             content.content_area.content = ft.Column([
#                 ft.Text("Настройки", size=25),
#                 ft.Switch(label="Включить что-то")
#             ])
#         self.content_area.update()

# a        = AdminPanel()
side_bar = SideBar()
content  = Content()