from src.repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def increment_stock(self, product_name: str, amount: int) -> bool:
        product = self.repository.find_by_name(product_name)
        product.stock += amount
        return self.repository.save(product)
