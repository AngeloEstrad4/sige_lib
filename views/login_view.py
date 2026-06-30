import flet as ft
from flet import Icons, Colors

def obtener_login_view(page: ft.Page, on_login_success):
    # Funciones de eventos del formulario
    def login_click(e):
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
            # Llamamos a la función que nos pasará main.py para cambiar de pantalla
            on_login_success()
        else:
            snack_bar = ft.SnackBar(
                content=ft.Text("Usuario o contraseña incorrectos.", color=Colors.WHITE),
                bg_color=Colors.RED_600
            )
            page.overlay.append(snack_bar)
            snack_bar.open = True
        
        page.update()

    # Componentes de la Interfaz Gráfica
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

    # Retornamos el contenedor del login envuelto en un Control para que main.py lo renderice
    return ft.Container(
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
        bgcolor=Colors.SURFACE,
        alignment=ft.alignment.center
    )