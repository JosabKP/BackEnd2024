from mi_tienda_libros.main import agregar_libro
from mi_tienda_libros.main import mostrar_inventario

inventario=[]

def agregar_libro():
    titulo=input("Ingrese el nombre del libro")
    autor=input("Ingrese el nombre del autor")
    publicacion=input("Ingrese el año de publicacion")
    inventario.append({'titulo': titulo, 'autor': autor, 'año publicacion': publicacion})
    print(f"Libro '{titulo}' agregado al inventario.")

def mostrar_inventario():
    """Muestra el inventario de libros"""
    if not inventario:
        print("El inventario está vacío.")
        return
    print("\n--- Inventario de libros ---")
    for i, libro in enumerate(inventario, start=1):
        print(f"{i}. Título: {libro['titulo']}, Autor: {libro['autor']}, Año de publicacion: {libro['año publicacion']}")


