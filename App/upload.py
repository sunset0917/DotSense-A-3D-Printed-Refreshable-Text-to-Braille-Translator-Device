import flet as ft
import time
from firebase_config import get_bucket, obtener_url_archivo
from procesamiento import procesar_desde_url
def upload_page(page: ft.Page):
    page.title = "Processing"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    archivo_nombre = page.client_storage.get("uploaded_file") or "Archivo desconocido"

    bucket = get_bucket()
    archivo_url = obtener_url_archivo(bucket, archivo_nombre)
    extension = archivo_nombre.split('.')[-1].lower() 
    print(extension)
    if archivo_url:


        text, braille, angulos = procesar_desde_url(archivo_url,archivo_nombre)
        print("Cantidad de angulos",len(angulos))

        if text and braille and angulos:
            page.add(
                ft.Column(
                    [
                        ft.Text("File processed successfully.", size=24, weight=ft.FontWeight.BOLD),
                        ft.Text(f"File Name: {archivo_nombre}", size=18),

                        ft.Text("Translating to Braille...",size=18),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                )
            )
        else:
            page.add(ft.Text("Error processing file.", color="red"))
    else:
        page.add(ft.Text("Error obtaining file's URL", color="red"))

    page.update()


