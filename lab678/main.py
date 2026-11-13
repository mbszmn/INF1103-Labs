from supplier import Supplier
from product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from inventory import Inventory
from order import Order

# tests(LSP) and Polymorphism
def show_product_details(product: Product) -> None:
    product.display_information()
    print(f"Fulfillment: {product.get_fulfilment_info()}")
    print("-" * 40)

def main():
    #1. Test Association. Supplier & Product can exist own their own
    tech_corp = Supplier("S001", "TechCorp", "sales@techcorp.com")
    book_dist = Supplier("S002", "BookDist", "orders@bookdist.com")

    phys_prod = PhysicalProduct("P001", "Gaming Mouse", 49.99, 100, tech_corp, 0.2)
    digi_prod = DigitalProduct("D001", "E-Book", 19.99, 999, book_dist, 5.0)

    #2. Test Aggregation. Inventory holds Products, but doesn't own their lifecycle
    inventory_a = Inventory()
    inventory_a.add_product(phys_prod)
    inventory_a.add_product(digi_prod)
    
    #3. Test Composition. Order creates and owns OrderLines
    order1 = Order("ORD-999")
    order1.add_order_line(phys_prod, 2)
    order1.add_order_line(digi_prod, 1)
    
    print("=== Testing Composition (Orders) ===")
    order1.display_order()

    #4. Test Polymorphism & LSP. Treating all child classes as generic product class
    print("\n=== Testing Polymorphism & LSP ===")
    for product in inventory_a.products:
        show_product_details(product)

if __name__ == "__main__":
    main()