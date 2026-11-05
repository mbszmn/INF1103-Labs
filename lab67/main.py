import json
import os
from product import PhysicalProduct, DigitalProduct
from inventory import Inventory

DATA_FILE = "inventory.json"

def load_inventory(inventory: Inventory) -> None:
    if not os.path.exists(DATA_FILE):
        return
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            for item in data:
                if item.get("type") == "physical":
                    prod = PhysicalProduct(item["product_id"], item["name"], item["price"], item["stock"], item["weight"])
                elif item.get("type") == "digital":
                    prod = DigitalProduct(item["product_id"], item["name"], item["price"], item["stock"], item["download_size"])
                else:
                    continue 
                inventory.add_product(prod)
    except Exception as e:
        print(f"Error loading inventory file: {e}")

def save_inventory(inventory: Inventory) -> None:
    data = [prod.to_dict() for prod in inventory.get_all_products()]
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
        print("Inventory saved successfully to inventory.json.")
    except Exception as e:
        print(f"Error saving inventory: {e}")

def main():
    inventory = Inventory()
    load_inventory(inventory)

    while True:
        print("\n=== Inventory Management System ===")
        print("1. Display all products")
        print("2. Add a product")
        print("3. Update stock")
        print("4. Search for a product")
        print("5. Save inventory")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            ptype = input("Enter product type (1 for Physical, 2 for Digital): ").strip()
            if ptype not in ["1", "2"]:
                print("Invalid product type. Returning to menu.")
                continue

            pid = input("Enter Product ID: ").strip()
            name = input("Enter Product Name: ").strip()
            try:
                price = float(input("Enter Price: "))
                stock = int(input("Enter Stock Quantity: "))
                
                # Prompt for subclass attributes
                if ptype == "1":
                    weight = float(input("Enter Weight (kg): "))
                    new_prod = PhysicalProduct(pid, name, price, stock, weight)
                elif ptype == "2":
                    size = float(input("Enter Download Size (MB): "))
                    new_prod = DigitalProduct(pid, name, price, stock, size)

                if inventory.add_product(new_prod):
                    print(f"Product '{name}' added successfully.")
            except ValueError:
                print("Invalid numerical input. Operation cancelled.")

        elif choice == "3":
            pid = input("Enter Product ID to update: ").strip()
            prod = inventory.search_product(pid)
            if prod:
                try:
                    qty = int(input("Enter quantity change (+ to add, - to subtract): "))
                    prod.update_stock(qty)
                    print("Stock updated successfully.")
                except ValueError:
                    print("Invalid quantity input.")
            else:
                print("Product not found.")

        elif choice == "4":
            pid = input("Enter Product ID to search: ").strip()
            prod = inventory.search_product(pid)
            if prod:
                prod.display_information()
                print(f"Fulfillment: {prod.get_fulfilment_info()}")
                # Demonstrate interface capability safely
                if hasattr(prod, 'calculate_shipping_cost'):
                    print(f"Shipping Cost: ${prod.calculate_shipping_cost():.2f}")
            else:
                print("Product not found.")

        elif choice == "5":
            save_inventory(inventory)

        elif choice == "6":
            print("Exiting application...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()