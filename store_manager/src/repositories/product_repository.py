from abc import ABC, abstractmethod

class ProductRepository(ABC):
    @abstractmethod
    def find_by_name (self, name: str):
        pass

    @abstractmethod
    def save(self, product):
        pass
    