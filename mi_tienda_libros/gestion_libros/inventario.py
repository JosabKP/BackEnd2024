inventario = []

def agregar_libro():
    """Agrega un libro al inventario"""
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    precio = float(input("Ingrese el precio del libro: "))
    inventario.append({'titulo': titulo, 'autor': autor, 'precio': precio})
    print(f"Libro '{titulo}' agregado al inventario.")

def mostrar_inventario():
    """Muestra el inventario de libros"""
    if not inventario:
        print("El inventario está vacío.")
        return
    print("\n--- Inventario de libros ---")
    for i, libro in enumerate(inventario, start=1):
        print(f"{i}. Título: {libro['titulo']}, Autor: {libro['autor']}, Precio: {libro['precio']:.2f}")
