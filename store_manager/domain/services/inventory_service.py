# domain/services/inventory_service.py
class InventoryService:
    def __init__(self, repository):
        self.repository = repository  # Inversión de Dependencias (SOLID)

    def add_product(self, product):
        # Lógica de negocio (Responsabilidad Única - SOLID)
        self.repository.add(product)  # Delegamos la persistencia al repositorio