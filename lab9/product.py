from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock_quantity: int, supplier: Supplier):
        self._product_id: str = product_id
        self._name: str = name
        self._price: float = price
        self._stock_quantity: int = stock_quantity
        self._supplier: Supplier = supplier  

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass

    def display_information(self) -> None:
        print(f"ID: {self._product_id} | Name: {self._name} | Price: ${self._price:.2f} | Stock: {self._stock_quantity}")
        print("Supplier Info: ", end="")
        self._supplier.display_information()