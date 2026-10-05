# 1. Data Representation
# Represent inventory items using dictionaries and store at least three products in a list.

inventory = [
    {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25}
]

# Data Manipulation
def display_all():
    print("\nCurrent Inventory")
    for item in inventory:
        print(f"ID: {item['id']} | Name: {item['name']} | Price: ${item['price']:.2f} | Stock: {item['stock']}")

def add_product():
    print("\nAdd New Product")
    p_id = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))
    inventory.append({"id": p_id, "name": name, "price": price, "stock": stock})
    print("Product added successfully!")       

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
            print("\nStock updated successfully!")
            return
    print("\nProduct not found.") 