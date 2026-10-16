import flet as ft

def settings_page(page: ft.Page):
    page.title = "Ajustes"
    page.clean()  # Limpiar la página actual

    # Botón de Volver (ahora navega a la ruta raíz "/")
    def back_click(e):
        page.go("/")

    back_button = ft.ElevatedButton(
        "← Volver",
        bgcolor="#e61548",
        color="white",
        on_click=back_click,
        width=200,
    )

    # Botón de Contraste
    def toggle_contrast(e):
        page.bgcolor = "#000000" if page.bgcolor != "#000000" else "#4c5f92"
        page.update()

    contrast_button = ft.ElevatedButton(
        "Modo Contraste",
        on_click=toggle_contrast,
        width=200,
    )

    # Diseño
    page.add(
        ft.Column(
            [
                back_button,
                ft.Text("Ajustes", size=24),
                contrast_button,
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
