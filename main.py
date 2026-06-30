import flet as ft
from flet import Icons, Colors
import bcrypt

def main(page: ft.Page):
    # Configuración de la ventana principal
    page.title = "SIGE-LIB - Inicio de Sesión"
    page.window_width = 450
    page.window_height = 600
    page.window_resizable = False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK  # Modo oscuro
    
    # Funciones de eventos
    def login_click(e):
        # Validación básica de campos vacíos
        if not txt_user.value or not txt_password.value:
            snack_bar = ft.SnackBar(
                content=ft.Text("Por favor, rellene todos los campos.", color=Colors.WHITE),
                bg_color=Colors.RED_ACCENT_700
            )
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
            return
        
        # Simulación temporal de credenciales
        if txt_user.value == "admin" and txt_password.value == "1234":
            page.clean()
            page.add(
                ft.Column(
                    [
                        ft.Icon(Icons.CHECK_CIRCLE_OUTLINE, color=Colors.GREEN, size=60),
                        ft.Text("¡Bienvenido al Sistema!", size=24, weight=ft.FontWeight.BOLD),
                        ft.Text("Acceso concedido a SIGE-LIB", size=16, color=Colors.GREY_400),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        else:
            snack_bar = ft.SnackBar(
                content=ft.Text("Usuario o contraseña incorrectos.", color=Colors.WHITE),
                bg_color=Colors.RED_600
            )
            page.overlay.append(snack_bar)
            snack_bar.open = True
        
        page.update()

    # Componentes de la Interfaz Gráfica (UI)
    logo_icon = ft.Icon(Icons.LOCAL_LIBRARY_ROUNDED, size=80, color=Colors.BLUE_ACCENT)
    
    titulo = ft.Text(
        "SIGE-LIB", 
        size=32, 
        weight=ft.FontWeight.BOLD, 
        color=Colors.BLUE_ACCENT_200
    )
    
    subtitulo = ft.Text(
        "Gestión de Inventario y Biblioteca", 
        size=14, 
        color=Colors.GREY_400,
        italic=True
    )

    txt_user = ft.TextField(
        label="Usuario o Correo",
        prefix_icon=Icons.PERSON,
        border_radius=10,
        width=320,
        focused_border_color=Colors.BLUE_ACCENT
    )

    txt_password = ft.TextField(
        label="Contraseña",
        prefix_icon=Icons.LOCK,
        password=True,
        can_reveal_password=True,
        border_radius=10,
        width=320,
        focused_border_color=Colors.BLUE_ACCENT,
        on_submit=login_click
    )

    btn_login = ft.ElevatedButton(
        text="Iniciar Sesión",
        width=320,
        height=50,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            color=Colors.WHITE,
            bgcolor=Colors.BLUE_ACCENT_700,
        ),
        on_click=login_click
    )

    # Contenedor del formulario - Cambiado a Colors.SURFACE que es totalmente seguro
    card_login = ft.Container(
        content=ft.Column(
            [
                logo_icon,
                ft.Column([titulo, subtitulo], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2),
                ft.Container(height=20),
                txt_user,
                txt_password,
                ft.Container(height=10),
                btn_login
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        ),
        padding=30,
        border_radius=15,
        bgcolor=Colors.SURFACE,  # <-- Solución al error
        alignment=ft.alignment.center
    )

    page.add(card_login)

if __name__ == "__main__":
    ft.app(target=main)