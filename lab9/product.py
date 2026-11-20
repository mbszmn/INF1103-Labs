from abc import ABC, abstractmethod
from supplier import Supplier

# Abstract base class for all products in the inventory
class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock_quantity: int, supplier: Supplier):
        # Validate that product price is greater than zero
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        # Validate that initial stock quantity is not negative
        if stock_quantity < 0:
            raise ValueError("Stock quantity cannot be negative.")

        self.product_id = product_id
        self.name = name
        self.price = float(price)
        self.stock_quantity = int(stock_quantity)
        self.supplier = supplier

    def update_stock(self, change: int) -> None:
        # Prevent stock from dropping below zero during updates
        if self.stock_quantity + change < 0:
            raise ValueError("Stock quantity cannot be negative.")
        self.stock_quantity += change

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        # Return delivery or fulfilment instructions for this product
        pass

    def display_information(self) -> None:
        # Print basic product details and supplier info
        print(f"ID: {self.product_id} | Name: {self.name} | Price: ${self.price:.2f} | Stock: {self.stock_quantity}")
        self.supplier.display_information()


# Concrete subclass for physical items that need shipping
class PhysicalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock_quantity: int, supplier: Supplier, weight: float = 1.0):
        super().__init__(product_id, name, price, stock_quantity, supplier)
        self.weight = weight

    def get_fulfilment_info(self) -> str:
        return f"Physical Delivery: {self.name} ({self.weight}kg) shipped via courier."


# Concrete subclass for digital items delivered online
class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock_quantity: int, supplier: Supplier, download_size: float = 0.0):
        super().__init__(product_id, name, price, stock_quantity, supplier)
        self.download_size = download_size

    def get_fulfilment_info(self) -> str:
        return f"Digital Delivery: {self.name} ({self.download_size}MB) download link sent via email."


# Factory class that centralises creation of Product subclasses
class ProductFactory:
    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float,
               stock_quantity: int, supplier: Supplier,
               weight: float = 1.0, download_size: float = 0.0) -> Product:
        # Clean the product type string before checking
        clean_type = product_type.strip().lower()

        if clean_type == "physical":
            return PhysicalProduct(product_id, name, price, stock_quantity, supplier, weight)
        elif clean_type == "digital":
            return DigitalProduct(product_id, name, price, stock_quantity, supplier, download_size)
        else:
            # Reject unknown product types with a clear error message
            raise ValueError(f"Unknown product type: {product_type}")