ventas = 0
from mi_tienda_libros.gestion_libros.inventario import inventario

def vender_libro():
    """Vende un libro del inventario"""
    if not inventario:
        print("El inventario está vacío. No se pueden realizar ventas.")
        return
    from mi_tienda_libros.gestion_libros.inventario import mostrar_inventario
    mostrar_inventario()
    try:
        eleccion = int(input("Ingrese el número del libro que desea vender: ")) - 1
        if 0 <= eleccion < len(inventario):
            libro = inventario.pop(eleccion)
            global ventas
            ventas += libro['precio']
            print(f"Libro '{libro['titulo']}' vendido por {libro['precio']:.2f}.")
        else:
            print("Número de libro no válido.")
    except (ValueError, IndexError):
        print("Entrada no válida. Inténtalo de nuevo.")

def mostrar_total_ventas():
    """Muestra el total de ventas"""
    print(f"Total de ventas: {ventas:.2f}")
