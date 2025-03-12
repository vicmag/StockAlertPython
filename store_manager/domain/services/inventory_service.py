# domain/services/inventory_service.py
from store_manager.domain.models.product import Product  # Importar la clase Product

class InventoryService:
    def __init__(self, repository):
        self.repository = repository  # Inversión de Dependencias (SOLID)

    def add_product(self, product):
        """
        Agrega un producto al inventario.
        
        Args:
            product (Product): El producto a agregar.
        """
        if not product or not isinstance(product, Product):
            raise ValueError("El producto no es válido.")
        
        self.repository.add(product)  # Delegamos la persistencia al repositorio