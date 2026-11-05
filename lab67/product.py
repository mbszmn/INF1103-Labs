from abc import ABC, abstractmethod

class Product(ABC):
    # Create constructor w the 4 attributes
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self._product_id = product_id
        self._name = name
        self._price = float(price)
        self._stock = int(stock)

    # Method 1: update stock
    def update_stock(self, quantity: int) 
        if self._stock + quantity < 0:
            print("Error: Stock level cannot fall below zero.")
        else:
            self._stock += quantity

    # Method 2: display information 
    def display_information(self) 
        print(f"ID: {self._product_id} | Name: {self._name:<15} | Price: ${self._price:>7.2f} | Stock: {self._stock:>4}, end="")

    # add abstract method
    ## fulfilment abstract method
    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass

    ## enforce dictionary method for json saving
    @abstractmethod
    def to_dict(self) -> dict:
        pass

    # Getters
    def get_product_id(self) -> str:
        return self._product_id

    def get_name(self) -> str:
        return self._name

    def get_price(self) -> float:
        return self._price

    def get_stock(self) -> int:
        return self._stock

# Interface
class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        pass

