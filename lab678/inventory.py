from product import Product

class Inventory:
    def __init__(self):
        self._products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self._products.append(product)

    def remove_product(self, product_id: str) -> None:
        product = self.find_product(product_id)
        if product:
            self._products.remove(product)

    def find_product(self, product_id: str) -> Product | None:
        for product in self._products:
            if product._product_id == product_id:
                return product
        return None

    def display_all_products(self) -> None:
        for product in self._products:
            product.display_information()