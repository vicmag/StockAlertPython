from src.repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self, repository: PendingDeprecationWarning):
        self.repository = repository

    def increment_stock(self, name: str, increment: int) -> bool:
        raise NotImplementedError("Fase Roja")
        