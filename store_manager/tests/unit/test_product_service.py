

class TestProductService:
    def test_increment_stock_should_update_product(self, mocker):
        # Arrange (configuración)
        mock_repository = mocker.Mock()
        product = Product(name="Camiseta", stock=10)

        # Configuración del comportamiento del mock
        mock_repository.find_by_name.return_value = product
        mock_repository.save.return_value = True

        service = ProductService(mock_repository)

        # Act (ejecucción)
        result = service.increment_stock("Camiseta", 5)

        # Assert (validación)
        mock_repository.find_by_name.assert_called_once_with("Camiseta")
        mock_repository.save.assert_called_once()
        _, args, _ = mock_repository.save.mock_calls[0]
        assert args[0].stock == 15

