from product import Product

class Inventory:
    def __init__(self):
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, product_id: str) -> None:
        product = self.find_product(product_id)
        if product:
            self.products.remove(product)

    def find_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def display_all_products(self) -> None:
        for product in self.products:
            product.display_information()