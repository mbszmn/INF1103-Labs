class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float):
        super().__init__(product_id, name, price, stock)
        self._weight = float(weight)

    def display_information(self):
        super().display_information()
        print(f" | Weight: {self._weight}kg")

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return self._weight * 5.0

    def to_dict(self) -> dict:
        return {
            "type": "physical",
            "product_id": self._product_id,
            "name": self._name,
            "price": self._price,
            "stock": self._stock,
            "weight": self._weight
            }