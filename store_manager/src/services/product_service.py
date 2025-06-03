from src.repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self, repository: PendingDeprecationWarning):
        self.repository = repository

    def increment_stock(self, name: str, increment: int) -> bool:
        product = self.repository.find_by_name(name)
        product.stock += increment
        return self.repository.save(product)
        