def limpiar_pantalla():
    """Limpia la pantalla de la terminal"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
