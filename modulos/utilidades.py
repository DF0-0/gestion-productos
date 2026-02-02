def validar_numero(mensaje, tipo=float):
    """
    Solicita un valor numérico al usuario y valida que sea positivo.

    Args:
        mensaje (str): Prompt para el input.
        tipo (type): Tipo de dato esperado (int o float).

    Returns:
        Numero positivo del tipo especificado.
    """
    while True:
        try:
            valor = tipo(input(mensaje))
            if valor < 0:
                print("Error: El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print(f"Error: Se requiere un dato de tipo {tipo.__name__}.")

def validar_texto(mensaje):
    """
    Solicita una cadena de texto y valida que no esté vacía.

    Args:
        mensaje (str): Prompt para el input.

    Returns:
        str: Cadena de texto validada.
    """
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Error: El campo no puede estar vacío.")

def calcular_valor_inventario_recursivo(lista_productos, index=0):
    """
    Calcula el valor total del inventario utilizando recursividad.

    Args:
        lista_productos (list): Lista de diccionarios de productos.
        index (int): Índice actual de la iteración recursiva.

    Returns:
        float: Sumatoria del valor total (precio * stock).
    """
    # Caso base: Fin de la lista
    if index == len(lista_productos):
        return 0.0

    producto = lista_productos[index]
    subtotal = producto['precio'] * producto['stock']

    # Llamada recursiva
    return subtotal + calcular_valor_inventario_recursivo(lista_productos, index + 1)