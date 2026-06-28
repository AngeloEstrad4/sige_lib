import flet as ft

def main(page: ft.Page):
    page.title = "SIGE-LIB - Prueba Inicial"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    texto = ft.Text("¡Entorno configurado con éxito en tu Mac!", size=24, weight=ft.FontWeight.BOLD)
    page.add(texto)

if __name__ == "__main__":
    ft.app(target=main)