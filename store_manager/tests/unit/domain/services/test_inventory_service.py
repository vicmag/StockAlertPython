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
        mock_alert_system = Mock()
        inventory_service = InventoryService(mock_repository, mock_alert_system)
        product = Product(id=1, name="Laptop", quantity=10, min_stock=10)

        # Ejecución del método a probar (principio de Responsabilidad Única - SOLID)
        inventory_service.add_product(product)

        # Verificación (principio de Abierto/Cerrado - SOLID)
        mock_repository.add.assert_called_once_with(product)

    def test_alert_low_stock(self):
        # Configuración de los mocks (principio de Inversión de Dependencias - SOLID)
        mock_repository = Mock()
        mock_alert_system = Mock()
        inventory_service = InventoryService(mock_repository, mock_alert_system)

        # Configurar el producto con stock bajo
        product = Product(id=1, name="Camiseta Azul", quantity=5, min_stock=10)

        # Ejecución del método a probar (principio de Responsabilidad Única - SOLID)
        inventory_service.check_stock_and_alert(product)

        # Verificación (principio de Abierto/Cerrado - SOLID)
        mock_alert_system.send_alert.assert_called_once_with(
            "Alerta de Stock Bajo",
            f"El producto 'Camiseta Azul' tiene un stock bajo. Cantidad actual: 5, Mínimo requerido: 10."
        )
 

if __name__ == '__main__':
    unittest.main()