from .utilidades import calcular_valor_inventario_recursivo

# Estructuras de datos en memoria
_inventario = []           # Base de datos principal
_nombres_registrados = set() # Índice de unicidad para nombres

def crear_producto(nombre, categoria, precio, stock):
    """
    Registra un nuevo producto en el sistema.
    Valida la unicidad del nombre mediante un conjunto hash.
    """
    if nombre.lower() in _nombres_registrados:
        return False, f"Conflicto: El producto '{nombre}' ya existe en el sistema."

    nuevo_producto = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    }

    _inventario.append(nuevo_producto)
    _nombres_registrados.add(nombre.lower())
    return True, "Registro exitoso."

def leer_inventario():
    """Retorna la lista completa de productos."""
    return _inventario

def buscar_producto_por_nombre(nombre):
    """Búsqueda lineal de producto por nombre."""
    for prod in _inventario:
        if prod['nombre'].lower() == nombre.lower():
            return prod
    return None

def actualizar_stock_producto(nombre, cantidad):
    """Modifica el atributo stock de un producto existente."""
    producto = buscar_producto_por_nombre(nombre)
    if producto:
        producto['stock'] = cantidad
        return True
    return False

def eliminar_producto(nombre):
    """Elimina un producto y actualiza el índice de unicidad."""
    producto = buscar_producto_por_nombre(nombre)
    if producto:
        _inventario.remove(producto)
        _nombres_registrados.remove(nombre.lower())
        return True
    return False

def obtener_metricas_financieras():
    """Interfaz para el cálculo recursivo del valor del inventario."""
    total_valor = calcular_valor_inventario_recursivo(_inventario)
    total_items = len(_inventario)
    return total_items, total_valor