from unittest import mock
import pytest
from src.models.product import Product
from src.services.product_service import ProductService

class TestProductService:
    def test_increment_stock_should_update_product(self, mocker):
        # Arrange (configuración)
        mock_repository = mocker.Mock()
        nameProduct = "Camiseta"
        initial_stock = 10
        increment = 5
        product = Product(name=nameProduct, stock=initial_stock)

        # Configuración del comportamiento del mock
        mock_repository.find_by_name.return_value = product
        mock_repository.save.return_value = True

        service = ProductService(mock_repository)

        # Act (ejecucción)
        result = service.increment_stock(nameProduct, increment)

        # Assert (validación)
        mock_repository.find_by_name.assert_called_once_with(nameProduct)
        mock_repository.save.assert_called_once()
        _, args, _ = mock_repository.save.mock_calls[0]
        assert args[0].stock == initial_stock + increment

