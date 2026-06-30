import flet as ft
from flet import Icons, Colors
# Importamos la función de la vista que acabamos de crear en la carpeta views
from views.login_view import obtener_login_view

def main(page: ft.Page):
    page.title = "SIGE-LIB - Sistema de Biblioteca"
    page.window_width = 450
    page.window_height = 600
    page.window_resizable = False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    # Acción que se ejecuta cuando el login es exitoso
    def ir_al_dashboard():
        page.clean()
        # Modificamos las dimensiones para la pantalla principal del sistema
        page.window_width = 1000
        page.window_height = 700
        page.window_resizable = True  # El sistema principal sí se puede estirar
        
        page.add(
            ft.Column(
                [
                    ft.Icon(Icons.CHECK_CIRCLE_OUTLINE, color=Colors.GREEN, size=60),
                    ft.Text("¡Bienvenido al Sistema Modular!", size=24, weight=ft.FontWeight.BOLD),
                    ft.Text("Aquí irá el menú y el inventario de libros.", size=16, color=Colors.GREY_400),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        page.update()

    # Cargamos la interfaz de login pasando la función de éxito como parámetro
    login_screen = obtener_login_view(page, on_login_success=ir_al_dashboard)
    
    # Mostramos el login al iniciar
    page.add(login_screen)

if __name__ == "__main__":
    ft.app(target=main)