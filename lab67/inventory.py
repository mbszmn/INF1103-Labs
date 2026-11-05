from product import Product

class Inventory:
    def __init__(self):
        self._products = {}  # list product attributes and values as a dictionary

    # Method 1
    def add_product(self, product: Product) -> bool:
        if product.get_product_id() in self._products:
            print(f"Error: Product ID '{product.get_product_id()}' already exists.")
            return False
        self._products[product.get_product_id()] = product
        return True

    # Method 2
    def search_product(self, product_id: str) -> Product:
        return self._products.get(product_id, None)

    # Method 3 
    def display_all(self) -> None:
        if not self._products:
            print("No products currently in inventory.")
            return
        print("\n--- Current Inventory ---")
        for product in self._products.values():
            product.display_information()

    def get_all_products(self) -> list[Product]:
        return list(self._products.values())