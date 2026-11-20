from product import Product

# Holds a collection of Product objects
class Inventory:
    def __init__(self):
        # Store products keyed by their product_id
        self.products: dict[str, Product] = {}

    def add_product(self, product: Product) -> None:
        # Add or overwrite a product in the inventory
        self.products[product.product_id] = product

    def get_product(self, product_id: str) -> Product | None:
        # Look up a product by ID
        return self.products.get(product_id)

    def display_all(self) -> None:
        # Display every product currently in the inventory
        for product in self.products.values():
            product.display_information()