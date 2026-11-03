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

    # Method 2: display information
    def display_information(self, product_id, name, price, stock):
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price} | Stock: {self.__stock}")

    # Getters
    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def get_stock(self):
        return self.__stock



    