from .utilidades import validar_numero, validar_texto
from .gestion import (
    crear_producto,
    leer_inventario,
    buscar_producto_por_nombre,
    eliminar_producto,
    actualizar_stock_producto,
    obtener_metricas_financieras
)

# Constante inmutable para categorías permitidas
CATEGORIAS_VALIDAS = ("Electronica", "Hogar", "Indumentaria", "Alimentos")

def mostrar_menu_principal():
    """Ejecuta el bucle principal de la aplicación."""
    ejecutando = True

    while ejecutando:
        print("\nSISTEMA DE GESTION DE INVENTARIO")
        print("=" * 32)
        print("1. Registrar nuevo producto")
        print("2. Listar inventario")
        print("3. Actualizar stock")
        print("4. Eliminar producto")
        print("5. Reporte de valoracion (Recursivo)")
        print("6. Salir")

        opcion = input("Seleccione operacion: ")

        if opcion == '1':
            _menu_registrar()
        elif opcion == '2':
            _menu_listar()
        elif opcion == '3':
            _menu_actualizar()
        elif opcion == '4':
            _menu_eliminar()
        elif opcion == '5':
            _menu_metricas()
        elif opcion == '6':
            print("Cerrando sesion. Finalizando procesos...")
            ejecutando = False
        else:
            print("Error: Comando no reconocido.")

def _menu_registrar():
    print("\n--- Registro de Producto ---")
    nombre = validar_texto("Nombre del producto: ")

    print(f"Categorias validas: {', '.join(CATEGORIAS_VALIDAS)}")
    while True:
        categoria = input("Categoria: ").capitalize()
        if categoria in CATEGORIAS_VALIDAS:
            break
        print("Error: Categoria no permitida.")

    precio = validar_numero("Precio unitario: ", float)
    stock = validar_numero("Stock inicial: ", int)

    exito, mensaje = crear_producto(nombre, categoria, precio, stock)
    print(f"Resultado: {mensaje}")

def _menu_listar():
    inventario = leer_inventario()
    if not inventario:
        print("Aviso: El inventario esta vacio.")
        return

    print(f"\n{'NOMBRE':<20} | {'CATEGORIA':<15} | {'PRECIO':<10} | {'STOCK':<5}")
    print("-" * 60)
    for p in inventario:
        print(f"{p['nombre']:<20} | {p['categoria']:<15} | {p['precio']:<10.2f} | {p['stock']:<5}")

def _menu_actualizar():
    nombre = validar_texto("Ingrese nombre del producto a modificar: ")
    if buscar_producto_por_nombre(nombre):
        nuevo_stock = validar_numero("Ingrese nuevo stock: ", int)
        actualizar_stock_producto(nombre, nuevo_stock)
        print("Exito: Stock actualizado.")
    else:
        print("Error: Producto no encontrado.")

def _menu_eliminar():
    nombre = validar_texto("Ingrese nombre del producto a eliminar: ")
    if eliminar_producto(nombre):
        print("Exito: Producto eliminado del sistema.")
    else:
        print("Error: Producto no inexistente.")

def _menu_metricas():
    cantidad, valor_total = obtener_metricas_financieras()
    print("\n--- Reporte Financiero ---")
    print(f"Total de items unicos: {cantidad}")
    print(f"Valoracion total (Algoritmo Recursivo): ${valor_total:,.2f}")