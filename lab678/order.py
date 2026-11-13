from product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int):
        self.product: Product = product
        self.quantity: int = quantity

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity

class Order:
    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        # Composition concept
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def calculate_total(self) -> float:
        return sum(line.calculate_subtotal() for line in self.order_lines)

    def display_order(self) -> None:
        print(f"\n--- Order: {self.order_id} ---")
        for line in self.order_lines:
            print(f"- {line.quantity}x {line.product.name} (@ ${line.product.price:.2f}): ${line.calculate_subtotal():.2f}")
        print(f"Total: ${self.calculate_total():.2f}\n")