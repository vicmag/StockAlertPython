from unittest.mock import Mock
import pytest
from src.models.product import Product
from src.services.product_service import ProductService

class TestProductService:
    def test_increment_stock_should_update_product_stock(self, mocker):
        # Arrange
        mock_repo = mocker.Mock()
        product = Product(name="Camiseta", stock=10)
        
        # Configurar mocks
        mock_repo.find_by_name.return_value = product
        mock_repo.save.return_value = True
        
        service = ProductService(mock_repo)
        
        # Act
        result = service.increment_stock("Camiseta", 5)
        
        # Assert
        assert result is True
        mock_repo.find_by_name.assert_called_once_with("Camiseta")
        mock_repo.save.assert_called_once()
        _, args, _ = mock_repo.save.mock_calls[0]
        assert args[0].stock == 15
        