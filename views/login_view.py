import flet as ft
from flet import Icons, Colors

def obtener_login_view(page: ft.Page, on_login_success):
    # ... (aquí mantienes tus funciones internas como login_click, etc.) ...

    # Elementos visuales que ya tienes en tu login (Logo, Textos, TextFields, Botón)
    logo = ft.Icon(Icons.BOOKMARK_ROUNDED, size=80, color=Colors.BLUE_ACCENT) # Tu logo actual
    titulo = ft.Text("SIGE-LIB", size=32, weight=ft.FontWeight.BOLD)
    subtitulo = ft.Text("Gestión de Inventario y Biblioteca", italic=True, color=Colors.GREY_400)
    
    txt_usuario = ft.TextField(label="Usuario o Correo", prefix_icon=Icons.PERSON)
    txt_contrasena = ft.TextField(label="Contraseña", prefix_icon=Icons.LOCK, password=True, can_reveal_password=True)
    btn_iniciar = ft.ElevatedButton("Iniciar Sesión", on_click=lambda _: on_login_success())

    # =========================================================================
    # LA SOLUCIÓN: Envolver todo en una columna con SCROLL activo
    # =========================================================================
    contenido_login = ft.Column(
        controls=[
            ft.Container(height=40), # Espacio superior
            logo,
            titulo,
            subtitulo,
            ft.Container(height=20), # Espacio intermedio
            txt_usuario,
            txt_contrasena,
            ft.Container(height=10),
            btn_iniciar,
            ft.Container(height=40), # Espacio inferior seguro
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15,
        scroll=ft.ScrollMode.AUTO # <- Esto activa la rueda del ratón si la ventana se achica
    )

    # Retornamos un contenedor que ocupe todo el espacio disponible de la pequeña ventana de login
    return ft.Container(
        content=contenido_login,
        alignment=ft.alignment.center,
        padding=30,
        expand=True # Se adapta dinámicamente al tamaño de la ventana
    )