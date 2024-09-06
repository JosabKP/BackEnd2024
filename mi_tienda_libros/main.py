from mi_tienda_libros.gestion_libros.inventario import agregar_libro, mostrar_inventario
from mi_tienda_libros.gestion_libros.ventas import vender_libro, mostrar_total_ventas
from mi_tienda_libros.utils import limpiar_pantalla

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n--- Menú de la tienda de libros ---")
    print("1. Agregar libro al inventario")
    print("2. Mostrar inventario")
    print("3. Vender libro")
    print("4. Mostrar total de ventas")
    print("5. Salir")

def ejecutar_opcion(opcion):
    """Ejecuta la opción seleccionada del menú"""
    if opcion == 1:
        agregar_libro()
    elif opcion == 2:
        mostrar_inventario()
    elif opcion == 3:
        vender_libro()
    elif opcion == 4:
        mostrar_total_ventas()
    elif opcion == 5:
        print("Saliendo...")
        return False  # Indica que el programa debe salir
    else:
        print("Opción no válida. Inténtalo de nuevo.")
    return True  # Indica que el programa debe seguir ejecutándose

def main():
    seguir = True
    while seguir:
        mostrar_menu()
        try:
            opcion = int(input("Selecciona una opción: "))
            seguir = ejecutar_opcion(opcion)
        except ValueError:
            print("Por favor, ingresa un número entero.")

if __name__ == "__main__":
    main()
