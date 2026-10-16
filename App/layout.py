import flet as ft
from app import home_page
from explore import explore_page
from upload import upload_page
from settings import settings_page

def main(page: ft.Page):
    page.title = "Mi App"
    page.window_width = 400
    page.window_height = 800
    page.window_resizable = False

    # Configura la navegación
    def route_change(e):
        page.views.clear()  # Limpiar vistas (no controles)
        
        if page.route == "/":
            home_page(page)
        elif page.route == "/explore":
            explore_page(page)
        elif page.route == "/upload":
            upload_page(page)
        elif page.route == "/settings":
            settings_page(page)
        else:
            page.views.append(ft.View("/404", [ft.Text("Página no encontrada")]))

    page.on_route_change = route_change
    page.go("/")  # Inicia en la página principal

ft.app(target=main)

