from product import Product
from supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock_quantity: int, supplier: Supplier, download_size: float):
        super().__init__(product_id, name, price, stock_quantity, supplier)
        self._download_size: float = download_size

    def display_information(self) -> None:
        super().display_information()
        print(f" | Size: {self._download_size}MB")

    def get_fulfilment_info(self) -> str:
        return f"Digital Delivery. Link sent via email."

    def to_dict(self) -> dict:
        return {
            "type": "digital",
            "product_id": self._product_id,
            "name": self._name,
            "price": self._price,
            "stock": self._stock,
            "download_size": self._download_size
        }

    