import flet as ft

# Página principal
def home_page(page: ft.Page):
    page.title = "Home"
    page.bgcolor = "#4c5f92"
    page.padding = 16

    # Títulos
    title = ft.Text("DOT SENSE", size=32, weight="bold", color="#FFFFFF")
    subtitle = ft.Text("Text to braille translator", size=18, color="#FFFFFF")

    # Botón de Start
    def on_button_click(e):
        page.go("/explore")  # Navegar a la página "explore"

    button = ft.ElevatedButton(
        text="Start",
        bgcolor="#e61548",
        color="#FFFFFF",
        on_click=on_button_click,
        style=ft.ButtonStyle(
            padding={"top": 12, "bottom": 12, "left": 24, "right": 24},
            shape=ft.RoundedRectangleBorder(radius=24),
        )
    )

    # Navegar a la página de ajustes al hacer clic en el botón de ajustes
    def open_settings(e):
        page.go("/settings")  # Navegar a la página de ajustes

    settings_button = ft.IconButton(
        icon=ft.icons.SETTINGS,
        tooltip="Ajustes",
        on_click=open_settings,
        icon_size=40,
    )

    # Agregar controles de la página dentro de un contenedor que se ajusta a toda la página
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[title, subtitle, button],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=32,
            ),
            alignment=ft.alignment.center,  # Asegura que el contenido esté centrado
            expand=True,  # Expande el contenedor para ocupar toda la página
        )
    )

    # Agregar el botón de ajustes en la parte superior derecha
    page.overlay.append(
        ft.Container(
            content=settings_button,
            alignment=ft.alignment.top_right,
            margin=ft.margin.only(top=10, right=10),
        )
    )

    page.update()  # Asegúrate de que la página se actualice correctamente

# Página de ajustes
def settings_page(page: ft.Page):
    page.title = "Ajustes"
    page.bgcolor = "#4c5f92"
    page.padding = 16

    # Títulos
    title = ft.Text("Ajustes", size=32, weight="bold", color="#FFFFFF")
    subtitle = ft.Text("Configura tus preferencias", size=18, color="#FFFFFF")

    # Botón de retroceso a la página principal
    def on_back_click(e):
        page.go("/")  # Regresar a la página principal

    back_button = ft.ElevatedButton(
        text="Volver",
        bgcolor="#e61548",
        color="#FFFFFF",
        on_click=on_back_click,
        style=ft.ButtonStyle(
            padding={"top": 12, "bottom": 12, "left": 24, "right": 24},
            shape=ft.RoundedRectangleBorder(radius=24),
        )
    )

    # Contenido de la página de ajustes dentro de un contenedor que se ajusta a toda la página
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[title, subtitle, back_button],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=32,
            ),
            alignment=ft.alignment.center,  # Asegura que el contenido esté centrado
            expand=True,  # Expande el contenedor para ocupar toda la página
        )
    )

    page.update()  # Asegúrate de que la página se actualice correctamente




