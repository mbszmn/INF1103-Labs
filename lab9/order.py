from product import Product
from discount import DiscountStrategy, NoDiscount

# Represents one product item and its quantity inside an order
class OrderLine:
    def __init__(self, product: Product, quantity: int):
        # Validate that order quantity is greater than zero
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.product = product
        self.quantity = quantity

    def calculate_subtotal(self) -> float:
        # Multiply product price by quantity
        return self.product.price * self.quantity


# Represents a customer order that uses an interchangeable discount strategy
class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy | None = None):
        self.order_id = order_id
        self.order_lines: list[OrderLine] = []
        # Default to NoDiscount if no strategy is passed in
        self.discount: DiscountStrategy = discount if discount is not None else NoDiscount()

    def add_line(self, product: Product, quantity: int) -> None:
        # Create and add a new order line to this order
        self.order_lines.append(OrderLine(product, quantity))

    def set_discount(self, discount: DiscountStrategy) -> None:
        # Swap the active discount strategy at runtime
        self.discount = discount

    def calculate_total(self) -> float:
        # Sum all line subtotals and pass the result to the active strategy
        total = sum(line.calculate_subtotal() for line in self.order_lines)
        return self.discount.apply(total)