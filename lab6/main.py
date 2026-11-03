import json
import os
from product import Product
from inventory import Inventory

DATA_FILE = "inventory.json"

def load_inventory(inventory: Inventory) -> None:
    if not os.path.exists(DATA_FILE):
        return
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            for item in data:
                prod = Product(item["product_id"], item["name"], item["price"], item["stock"])
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

def main():
    inventory = Inventory() 

    product1 = Product("P001", "Laptop", 1200.00, 15) 
    product2 = Product("P002", "Mouse", 25.50, 40)

    inventory.add_product(product1)
    inventory.add_product(product2)

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
            pid = input("Enter Product ID: ").strip()
            name = input("Enter Product Name: ").strip()
            try:
                price = float(input("Enter Price: "))
                stock = int(input("Enter Stock Quantity: "))
                new_prod = Product(pid, name, price, stock)
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