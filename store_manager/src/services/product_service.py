from src.repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository
        
    def increment_stock(self, product_name: str, amount: int) -> bool:
        raise NotImplementedError("Not implemented yet")