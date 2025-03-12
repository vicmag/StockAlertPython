# infrastructure/repositories/inventory_repository.py
class InventoryRepository:
    def __init__(self):
        self.products = []  # Simulamos una base de datos en memoria

    def add(self, product):
        """
        Agrega un producto a la lista de productos.
        
        Args:
            product (Product): El producto a agregar.
        """
        if not product or not hasattr(product, 'id'):
            raise ValueError("El producto no es válido.")
        
        self.products.append(product)

    def update_stock(self, product, new_quantity):
        """
        Actualiza el stock de un producto.
        
        Args:
            product (Product): El producto a actualizar.
            new_quantity (int): La nueva cantidad de stock.
        """
        pass  # Implementación pendiente