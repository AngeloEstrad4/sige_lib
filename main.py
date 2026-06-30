import flet as ft
from views.login_view import obtener_login_view
from views.dashboard_view import obtener_dashboard_view

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.user_data = {"pantalla_actual": "login"}

    # --- CONTROL DINÁMICO DE PANTALLA ---
    def vigilar_tamano_ventana(e):
        if page.user_data["pantalla_actual"] == "login":
            if page.window_width != 450 or page.window_height != 600:
                page.window_width = 450
                page.window_height = 600
                page.update()
        
        elif page.user_data["pantalla_actual"] == "dashboard":
            MODIF_REQUERIDA = False
            if page.window_width < 1100:
                page.window_width = 1100
                MODIF_REQUERIDA = True
            if page.window_height < 500:  # Permite achicar para activar el scroll
                page.window_height = 500
                MODIF_REQUERIDA = True
                
            if MODIF_REQUERIDA:
                page.update()

    page.on_resize = vigilar_tamano_ventana

    # --- ENRUTAMIENTO ---
    def cerrar_sesion():
        page.clean()
        page.user_data["pantalla_actual"] = "login"
        page.window_width = 450
        page.window_height = 600
        page.window_resizable = False
        
        login_screen = obtener_login_view(page, on_login_success=ir_al_dashboard)
        page.add(login_screen)
        page.update()

    def ir_al_dashboard():
        page.clean()
        page.user_data["pantalla_actual"] = "dashboard"
        
        # Dimensiones estándar comerciales óptimas
        page.window_resizable = True
        page.window_width = 1280
        page.window_height = 800
        page.update() 
        
        dashboard_screen = obtener_dashboard_view(page, on_logout=cerrar_sesion)
        page.add(dashboard_screen)
        page.update()

    # --- CONFIGURACIÓN DE INICIO ---
    page.title = "SIGE-LIB - Sistema de Inventario y Ventas"
    page.window_width = 450
    page.window_height = 600
    page.window_resizable = False

    login_screen = obtener_login_view(page, on_login_success=ir_al_dashboard)
    page.add(login_screen)

if __name__ == "__main__":
    ft.app(target=main)