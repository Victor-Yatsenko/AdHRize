import flet as ft
from client import autorization, form
from client.admin_panel import admin_panel
from client.admin_panel.section_of_admin_panel import add_new_form



def route_change(e: ft.RouteChangeEvent):
    e.page.clean()
    route = e.page.route
    match route:
        case "/":
            autoriz = autorization.Autorization(e.page)
            e.page.add(autoriz.view)

        case "/form":
            e.page.add(ft.Row(controls=[form.f.form], alignment=ft.MainAxisAlignment.CENTER))

        case "/admin":
            panel    = admin_panel.AdminPanel(e.page, e)
            side_bar = admin_panel.SideBar()
            content  = admin_panel.Content(e.page)
            e.page.add(panel.build(side_bar, content))

        case "/admin/add_new_form":
            viev = add_new_form.AddNewForm(e.page)
            e.page.add(viev.add_new_form)