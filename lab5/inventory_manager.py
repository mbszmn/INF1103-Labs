import json
import os

inventory = []

# 3. Data Persistence
def load_inventory():
    global inventory
    if os.path.exists("inventory.json"):
        print("inventory.json found.")
        with open("inventory.json", "r") as file:
            inventory = json.load(file)
        print("Inventory loaded successfully.")
    else:
        # Load the three products cuz json doesnt exist yet
        inventory = [
            {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
            {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
            {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25}
        ]

# 1. Data Representation
# Represent inventory items using dictionaries and store at least three products in a list.

#inventory = [
#    {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
#    {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
#    {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25}
#]

# Data Manipulation
def display_all():
    print("\nCurrent Inventory")
    print("--------------------------------------------------")
    for item in inventory:
        print(f"ID: {item['id']} | Name: {item['name']} | Price: ${item['price']:.2f} | Stock: {item['stock']}")
    print("--------------------------------------------------\n")

def add_product():
    print("\nAdd New Product")
    p_id = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))
    inventory.append({"id": p_id, "name": name, "price": price, "stock": stock})
    print("\nProduct added successfully!\n")       

def update_stock():
    print("\nUpdate Stock")
    p_id = input("Enter Product ID: ")
    for item in inventory:
        if item['id'] == p_id:
            print("\nProduct Found:")
            print(f"Name: {item['name']}")
            print(f"Current Stock: {item['stock']}\n")
            new_stock = int(input("New Stock Quantity: "))
            item['stock'] = new_stock
            print("\nStock updated successfully!\n")
            return
    print("\nProduct not found.") 

def search_product():
    print("\nSearch Product")
    p_id = input("Enter Product ID: ")
    for item in inventory:
        if item['id'] == p_id:
            print("\nProduct Found")
            print("--------------------------------------------------")
            print(f"ID: {item['id']}")
            print(f"Name: {item['name']}")
            print(f"Price: ${item['price']:.2f}")
            print(f"Stock: {item['stock']}")
            print("--------------------------------------------------\n")
            return
    print("\nProduct not found.\n")

# 4. Build a Menu System
def save_inventory(is_exit=False):
    if is_exit:
        print("\nSaving inventory before exit...")
    else:
        print("\nSaving inventory...")
        
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)
        
    if is_exit:
        print("Inventory saved successfully.")
    else:
        print("Inventory saved successfully to inventory.json.\n")

# MAIN
def main():
    print("==================================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("==================================================\n")

    load_inventory()

    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------\n")

    while True:
        option = input("Enter option: ")

        if option == '1':
            display_all()
        elif option == '2':
            add_product()
        elif option == '3':
            update_stock()
        elif option == '4':
            search_product()
        elif option == '5':
            save_inventory()
        elif option == '6':
            save_inventory(is_exit=True)
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("\nInvalid option.")

if __name__ == "__main__":
    main()