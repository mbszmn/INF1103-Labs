from product import Product
from supplier import Supplier
from CanBeShipped import CanBeShipped


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock_quantity: int, supplier: Supplier, weight: float):
        super().__init__(product_id, name, price, stock_quantity, supplier)
        self._weight: float = weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Physical Attributes: Weight {self._weight}kg")

    def get_fulfilment_info(self) -> str:
        return f"Physical Delivery: Item weighs {self._weight}kg. Ships in standard packaging."
        
    def calculate_shipping_cost(self) -> float:
        return self._weight * 5.0