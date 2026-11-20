from supplier import Supplier
from product import ProductFactory
from inventory import Inventory
from order import Order
from discount import BulkDiscount, PercentageDiscount, StudentDiscount
from utils import load_products, get_positive_float

def main() -> None:
    # Create a default supplier
    supplier = Supplier("SUP01", "TechDistributors", "orders@techdist.com")
    inventory = Inventory()

    # Load products from CSV using ProductFactory and exception handling
    print("--- Loading Products from CSV ---")
    load_products("products.csv", inventory, supplier)

    # Display loaded products
    print("\n--- Current Inventory ---")
    inventory.display_all()

    # Demonstrate creating a product through ProductFactory
    print("\n--- Creating New Product via Factory ---")
    keyboard = ProductFactory.create("physical", "P004", "Mechanical Keyboard", 125.00, 15, supplier)
    inventory.add_product(keyboard)

    # Demonstrate Strategy pattern on an Order totaling 250.00
    print("\n--- Testing Discount Strategies ---")
    order = Order("ORD-1001", BulkDiscount(200, 20))
    order.add_line(keyboard, 2)  # 2 x 125.00 = 250.00
    print(f"Total with BulkDiscount(200, 20): ${order.calculate_total():.2f}")

    # Swap strategy at runtime to PercentageDiscount(10)
    order.set_discount(PercentageDiscount(10))
    print(f"Total after set_discount(PercentageDiscount(10)): ${order.calculate_total():.2f}")

    # Swap strategy to StudentDiscount (5% off)
    order.set_discount(StudentDiscount())
    print(f"Total after set_discount(StudentDiscount()): ${order.calculate_total():.2f}")

    # Demonstrate interactive positive float validation
    print("\n--- Testing Input Validation ---")
    custom_price = get_positive_float("Enter a positive price to test validation: ")
    print(f"Accepted valid price: ${custom_price:.2f}")

if __name__ == "__main__":
    main()