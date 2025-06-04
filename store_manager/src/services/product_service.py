from src.repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self, repository: PendingDeprecationWarning):
        self.repository = repository

    def increment_stock(self, name: str, increment: int) -> bool:
        product = self.repository.find_by_name(name)
        if product is None:
            raise ValueError("Producto no encontrado")
        
        if increment <= 0:
            raise ValueError("El incremento debe ser positivo")
        product.stock += increment        
        return self.repository.save(product)
        