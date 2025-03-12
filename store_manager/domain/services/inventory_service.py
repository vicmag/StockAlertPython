# domain/services/inventory_service.py
from store_manager.domain.models.product import Product  # Importar la clase Product

class InventoryService:
    def __init__(self, repository, alert_system):
        self.repository = repository  # Inversión de Dependencias (SOLID)
        self.alert_system = alert_system  # Inversión de Dependencias (SOLID)

    def add_product(self, product):
        """
        Agrega un producto al inventario.
        
        Args:
            product (Product): El producto a agregar.
        """
        if not product or not isinstance(product, Product):
            raise ValueError("El producto no es válido.")
        
        self.repository.add(product)  # Delegamos la persistencia al repositorio

    def check_stock_and_alert(self, product):
        """
        Verifica el stock de un producto y envía una alerta si está por debajo del nivel mínimo.
        
        Args:
            product (Product): El producto a verificar.
        """
        if product.quantity <= product.min_stock:
            self.alert_system.send_alert(
                "Alerta de Stock Bajo",
                f"El producto '{product.name}' tiene un stock bajo. Cantidad actual: {product.quantity}, Mínimo requerido: {product.min_stock}."
            )