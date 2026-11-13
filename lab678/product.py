from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock_quantity: int, supplier: Supplier):
        self.product_id: str = product_id
        self.name: str = name
        self.price: float = price
        self.stock_quantity: int = stock_quantity
        self.supplier: Supplier = supplier  

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass

    def display_information(self) -> None:
        print(f"ID: {self.product_id} | Name: {self.name} | Price: ${self.price:.2f} | Stock: {self.stock_quantity}")
        print("Supplier Info: ", end="")
        self.supplier.display_information()