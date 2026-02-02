# Sistema de Gestion de Productos - Modulo 3

## Descripcion General
Aplicacion de consola (CLI) desarrollada en Python para la gestion integral de inventario. El sistema implementa operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y calculos financieros mediante algoritmos recursivos, cumpliendo con los estandares de codificacion PEP 8 y buenas practicas de arquitectura de software.

## Especificaciones Tecnicas de Implementacion

El proyecto demuestra el dominio de las siguientes estructuras y conceptos:

### 1. Estructuras de Datos
* **Listas (list):** Utilizadas para la persistencia volatil de la base de datos de productos.
* **Diccionarios (dict):** Modelado de la entidad "Producto", permitiendo un acceso estructurado clave-valor a sus atributos.
* **Conjuntos (set):** Implementacion de un indice de unicidad para nombres de productos. Esto optimiza la validacion de duplicados reduciendo la complejidad temporal de busqueda a O(1).
* **Tuplas (tuple):** Definicion de datos inmutables para restringir el dominio de categorias validas.

### 2. Algoritmos y Control de Flujo
* **Recursividad:** Se implementa la funcion `calcular_valor_inventario_recursivo` en el modulo de utilidades para realizar la sumatoria del valor total del inventario sin utilizar bucles iterativos tradicionales.
* **Validacion Robusta:** Implementacion de bloques `try-except` para garantizar la integridad de los tipos de datos en entradas numericas (flotantes y enteros).
* **Modularizacion:** Arquitectura dividida en tres capas logicas:
    * `modulos/interfaz.py`: Capa de presentacion y menus.
    * `modulos/gestion.py`: Logica de negocio y manejo de datos.
    * `modulos/utilidades.py`: Funciones transversales y validaciones.

## Instrucciones de Despliegue y Ejecucion
Este sistema ha sido diseñado para ser ejecutado tanto desde un entorno local como mediante clonacion desde repositorio remoto.

### Requisitos Previos
Intérprete Python version 3.8 o superior instalado en el sistema.

### Opcion A: Ejecucion desde Repositorio Remoto (GitHub)
Para evaluar el proyecto directamente desde el control de versiones:

Abra su terminal o linea de comandos.

Clone el repositorio utilizando Git:

Bash
git clone https://github.com/DF0-0/gestion-productos
Acceda al directorio generado:

Bash
cd productos
(Nota: Verifique el nombre exacto de la carpeta generada tras la clonacion).

Ejecute el archivo principal:

Bash
python3 main.py

### Opcion B: Ejecucion Local (Archivos Fuente)
Si dispone de la carpeta del proyecto en su equipo:

Abra una terminal en la raiz del directorio del proyecto (donde se ubica main.py).

Ejecute el siguiente comando:

Bash python3 main.py
    Nota: En sistemas Windows, si el comando python3 no es reconocido, utilice python main.py.**


## Estructura del Proyecto

```text
proyecto_productos/
├── main.py                  # Punto de entrada (Orquestador)
├── README.md                # Documentacion tecnica
└── modulos/                 # Paquete de codigo fuente
    ├── __init__.py
    ├── gestion.py
    ├── interfaz.py
    └── utilidades.py


