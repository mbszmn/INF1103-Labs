class Product:

    # Create constructor w the 4 attributes
    def __init__(self, product_id:str, name:str, price:float, stock:int):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    # Method 1: update stock
    def update_stock(self, quantity : int):
        if self.__stock + quantity < 0:
            print("Error: Invalid stock quantity. Cannot reduce stock below zero.")
        else:
            self.__stock += quantity

    def display_information(self, product_id, name, price, stock):
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price} | Stock: {self.__stock}")

    # Getters
    