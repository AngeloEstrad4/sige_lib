import flet as ft
from flet import Icons, Colors

def obtener_dashboard_view(page: ft.Page, on_logout):
    """
    Estructura visual del Dashboard.
    Fija el NavigationRail dentro de un Column con altura controlada
    para evitar errores de desbordamiento y habilitar scroll con el mouse.
    """

    # ==========================================
    # 1. ENRUTADOR DE MÓDULOS
    # ==========================================
    def cambiar_pantalla(e):
        indice = e.control.selected_index
        
        if indice == 0: area_contenido.content = mostrar_inicio()
        elif indice == 1: area_contenido.content = mostrar_ventas()
        elif indice == 2: area_contenido.content = mostrar_caja()
        elif indice == 3: area_contenido.content = mostrar_inventario()
        elif indice == 4: area_contenido.content = mostrar_servicios()
        elif indice == 5: area_contenido.content = mostrar_promociones()
        elif indice == 6: area_contenido.content = mostrar_clientes()
        elif indice == 7: area_contenido.content = mostrar_cobranzas()
        elif indice == 8: area_contenido.content = mostrar_reportes()
        elif indice == 9: area_contenido.content = mostrar_configuracion()
        elif indice == 10:
            menu_lateral.selected_index = 0
            page.update()
            abrir_consulta_precios(None)
            return
        elif indice == 11:
            on_logout()
            return
            
        page.update()

    # ==========================================
    # 2. DIÁLOGO: CONSULTA DE PRECIOS
    # ==========================================
    def abrir_consulta_precios(e):
        txt_buscar = ft.TextField(
            label="Escriba nombre, código o use lector de barras...",
            prefix_icon=Icons.BARCODE_READER,
            autofocus=True,
            expand=True
        )
        tabla_resultado = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Producto")),
                ft.DataColumn(ft.Text("Categoría")),
                ft.DataColumn(ft.Text("Precio ($)")),
                ft.DataColumn(ft.Text("Stock")),
            ],
            rows=[]
        )
        dlg = ft.AlertDialog(
            title=ft.Text("Consulta Rápida de Precios", weight=ft.FontWeight.BOLD),
            content=ft.Container(
                content=ft.Column([
                    ft.Row([txt_buscar, ft.ElevatedButton("Buscar", icon=Icons.SEARCH, bgcolor=Colors.BLUE_ACCENT_700)]),
                    ft.Container(height=10),
                    tabla_resultado
                ], tight=True, scroll=ft.ScrollMode.AUTO),
                width=650, height=350
            ),
            actions=[ft.TextButton("Cerrar", on_click=lambda e: page.close(dlg))]
        )
        page.open(dlg)

    # ==========================================
    # 3. CONTENIDOS DE LAS VISTAS
    # ==========================================
    def mostrar_inicio():
        txt_tasa = ft.TextField(
            value="45.50", label="Tasa BCV (Bs.)", width=120, height=40, text_size=13, content_padding=10
        )
        return ft.Column([
            ft.Row([
                ft.Column([
                    ft.Text("Panel de Control", size=24, weight=ft.FontWeight.BOLD),
                    ft.Text("Monitoreo en tiempo real de la tienda universitaria.", size=14, color=Colors.GREY_400),
                ]),
                ft.ElevatedButton(
                    "Consultar Precio", icon=Icons.SEARCH_ROUNDED, bgcolor=Colors.BLUE_ACCENT_700,
                    color=Colors.WHITE, height=45, on_click=abrir_consulta_precios
                )
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            
            ft.Row([
                crear_tarjeta_metrica("Ventas del Día", "$240.50", Icons.ATTACH_MONEY, Colors.GREEN_ACCENT),
                ft.Container(
                    content=ft.Row([
                        ft.Icon(Icons.CURRENCY_EXCHANGE, size=30, color=Colors.ORANGE_ACCENT),
                        ft.Column([
                            ft.Text("Tasa del Día", size=12, color=Colors.GREY_400),
                            ft.Row([
                                txt_tasa,
                                ft.IconButton(icon=Icons.SAVE_ROUNDED, icon_color=Colors.BLUE_ACCENT, icon_size=20, on_click=lambda _: print(f"Tasa: {txt_tasa.value}"))
                            ], spacing=5)
                        ], spacing=1)
                    ]),
                    bgcolor=Colors.BLACK26, padding=12, border_radius=10, width=240, height=80
                )
            ], spacing=20),
            
            ft.Container(height=10),
            
            ft.Row([
                ft.Container(
                    content=ft.Column([
                        ft.Text("Últimas Ventas Realizadas", size=16, weight=ft.FontWeight.BOLD),
                        ft.DataTable(
                            columns=[ft.DataColumn(ft.Text("Hora")), ft.DataColumn(ft.Text("Cliente")), ft.DataColumn(ft.Text("Total ($)"))],
                            rows=[
                                ft.DataRow(cells=[ft.DataCell(ft.Text("10:30 AM")), ft.DataCell(ft.Text("Carlos P.")), ft.DataCell(ft.Text("$4.50"))]),
                                ft.DataRow(cells=[ft.DataCell(ft.Text("11:15 AM")), ft.DataCell(ft.Text("Ana M.")), ft.DataCell(ft.Text("$12.00"))]),
                            ]
                        )
                    ]),
                    bgcolor=Colors.BLACK12, padding=15, border_radius=10, expand=3
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Text("Reponer Stock (Bajo)", size=16, weight=ft.FontWeight.BOLD, color=Colors.RED_ACCENT_200),
                        ft.ListTile(leading=ft.Icon(Icons.WARNING_ROUNDED, color=Colors.RED_ACCENT), title=ft.Text("Lápices Cello"), subtitle=ft.Text("Quedan: 3 und", color=Colors.GREY_400)),
                        ft.ListTile(leading=ft.Icon(Icons.WARNING_ROUNDED, color=Colors.RED_ACCENT), title=ft.Text("Hojas de Examen"), subtitle=ft.Text("Quedan: 15 und", color=Colors.GREY_400))
                    ]),
                    bgcolor=Colors.BLACK12, padding=15, border_radius=10, expand=2
                )
            ], alignment=ft.MainAxisAlignment.START, vertical_alignment=ft.CrossAxisAlignment.START)
        ], spacing=15, scroll=ft.ScrollMode.AUTO)

    def mostrar_ventas(): return ft.Column([ft.Text("Punto de Venta (POS)", size=24, weight=ft.FontWeight.BOLD)])
    def mostrar_caja(): return ft.Column([ft.Text("Control de Caja Chica (Efectivo)", size=24, weight=ft.FontWeight.BOLD)])
    def mostrar_inventario(): return ft.Column([ft.Text("Estructura de Inventario", size=24, weight=ft.FontWeight.BOLD)])
    def mostrar_servicios(): return ft.Column([ft.Text("Módulo de Servicios", size=24, weight=ft.FontWeight.BOLD)])
    def mostrar_promociones(): return ft.Column([ft.Text("Combos y Promociones", size=24, weight=ft.FontWeight.BOLD)])
    def mostrar_clientes(): return ft.Column([ft.Text("Fichero de Clientes", size=24, weight=ft.FontWeight.BOLD)])
    def mostrar_cobranzas(): return ft.Column([ft.Text("Cuentas por Cobrar (Cobranzas)", size=24, weight=ft.FontWeight.BOLD, color=Colors.ORANGE_ACCENT_400), ft.Text("Monitoreo de clientes con ventas a crédito (Fiados).", size=14, color=Colors.GREY_400)])
    def mostrar_reportes(): return ft.Column([ft.Text("Reportes Estadísticos", size=24, weight=ft.FontWeight.BOLD)])
    def mostrar_configuracion(): return ft.Column([ft.Text("Configuración del Sistema", size=24, weight=ft.FontWeight.BOLD)])

    def crear_tarjeta_metrica(titulo, valor, icono, color_icono):
        return ft.Container(
            content=ft.Row([
                ft.Icon(icono, size=40, color=color_icono),
                ft.Column([ft.Text(titulo, size=14, color=Colors.GREY_400), ft.Text(valor, size=22, weight=ft.FontWeight.BOLD)], spacing=2)
            ], alignment=ft.MainAxisAlignment.START),
            bgcolor=Colors.BLACK26, padding=20, border_radius=10, width=230, height=85
        )

    # ==========================================
    # 4. INSTANCIACIÓN DEL MENÚ DE NAVEGACIÓN
    # ==========================================
    menu_lateral = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=140,
        group_alignment=-1.0, 
        destinations=[
            ft.NavigationRailDestination(icon=Icons.DASHBOARD_OUTLINED, selected_icon=Icons.DASHBOARD, label="Inicio"),
            ft.NavigationRailDestination(icon=Icons.POINT_OF_SALE, selected_icon=Icons.POINT_OF_SALE, label="Ventas"),
            ft.NavigationRailDestination(icon=Icons.PRICE_CHECK, selected_icon=Icons.PRICE_CHECK, label="Caja"),
            ft.NavigationRailDestination(icon=Icons.INVENTORY_2_OUTLINED, selected_icon=Icons.INVENTORY_2, label="Inventario"),
            ft.NavigationRailDestination(icon=Icons.PRINT_OUTLINED, selected_icon=Icons.PRINT, label="Servicios"),
            ft.NavigationRailDestination(icon=Icons.LOYALTY_OUTLINED, selected_icon=Icons.LOYALTY, label="Promos"),
            ft.NavigationRailDestination(icon=Icons.PEOPLE_OUTLINED, selected_icon=Icons.PEOPLE, label="Clientes"),
            ft.NavigationRailDestination(icon=Icons.CREDIT_CARD_OFF_OUTLINED, selected_icon=Icons.CREDIT_CARD_OFF, label="Cobranza"),
            ft.NavigationRailDestination(icon=Icons.ANALYTICS_OUTLINED, selected_icon=Icons.ANALYTICS, label="Reportes"),
            ft.NavigationRailDestination(icon=Icons.SETTINGS_OUTLINED, selected_icon=Icons.SETTINGS, label="Config."),
            ft.NavigationRailDestination(icon=Icons.MANAGE_SEARCH_ROUNDED, selected_icon=Icons.MANAGE_SEARCH_ROUNDED, label="Buscar P."),
            ft.NavigationRailDestination(icon=Icons.LOGOUT_ROUNDED, selected_icon=Icons.LOGOUT_ROUNDED, label="Salir"),
        ],
        on_change=cambiar_pantalla,
    )

    # ==========================================
    # 5. CONTENEDOR CENTRAL DE MÓDULOS
    # ==========================================
    area_contenido = ft.Container(
        content=mostrar_inicio(),
        expand=True,
        padding=30,
        bgcolor=Colors.SURFACE,
        border_radius=ft.border_radius.only(top_left=20)
    )

    # ==========================================
    # 6. ENVOLTORIO PROTECTOR DE MENÚ
    # ==========================================
    sidebar_protector = ft.Column(
        controls=[
            ft.Container(
                content=menu_lateral,
                height=760,  # Espacio suficiente para albergar los 12 elementos de forma segura
                width=105,
            )
        ],
        scroll=ft.ScrollMode.AUTO,  # Activa el scroll vertical con la rueda del ratón si la ventana se achica
        width=105,
    )

    return ft.Row(
        [
            sidebar_protector,
            ft.VerticalDivider(width=1, color=Colors.GREY_800),
            area_contenido,
        ],
        expand=True,
    )