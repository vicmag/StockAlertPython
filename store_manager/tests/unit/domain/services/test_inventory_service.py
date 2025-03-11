# tests/unit/domain/services/test_inventory_service.py
import unittest
from unittest.mock import Mock
from store_manager.domain.services.inventory_service import InventoryService
from store_manager.domain.models.product import Product
from store_manager.infrastructure.repositories.inventory_repository import InventoryRepository

class TestInventoryService(unittest.TestCase):
    def test_add_product_to_inventory(self):
        # Configuración del mock (principio de Inversión de Dependencias - SOLID)
        mock_repository = Mock(spec=InventoryRepository)
        inventory_service = InventoryService(mock_repository)
        product = Product(id=1, name="Laptop", quantity=10)

        # Ejecución del método a probar (principio de Responsabilidad Única - SOLID)
        inventory_service.add_product(product)

        # Verificación (principio de Abierto/Cerrado - SOLID)
        mock_repository.add.assert_called_once_with(product)

if __name__ == '__main__':
    unittest.main()