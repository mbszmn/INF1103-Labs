class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float):
        super().__init__(product_id, name, price, stock)
        self._download_size = float(download_size)

    def display_information(self) -> None:
        super().display_information()
        print(f" | Size: {self._download_size}MB")

    def get_fulfilment_info(self) -> str:
        return "This product is delivered digitally via a download link."

    def to_dict(self) -> dict:
        return {
            "type": "digital",
            "product_id": self._product_id,
            "name": self._name,
            "price": self._price,
            "stock": self._stock,
            "download_size": self._download_size
        }

    