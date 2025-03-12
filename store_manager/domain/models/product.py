# domain/models/product.py
class Product:
    def __init__(self, id, name, quantity):
        if not id or not isinstance(id, int):
            raise ValueError("El ID del producto debe ser un entero válido.")
        if not name or not isinstance(name, str):
            raise ValueError("El nombre del producto debe ser una cadena válida.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("La cantidad del producto debe ser un entero no negativo.")

        self.id = id
        self.name = name
        self.quantity = quantity