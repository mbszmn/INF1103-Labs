from product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int):
        self._product: Product = product
        self._quantity: int = quantity

    def calculate_subtotal(self) -> float:
        return self._product._price * self._quantity

class Order:
    def __init__(self, order_id: str):
        self._order_id: str = order_id
        self._order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self._order_lines.append(order_line)

    def calculate_total(self) -> float:
        return sum(line.calculate_subtotal() for line in self._order_lines)

    def display_order(self) -> None:
        print(f"\n--- Order: {self._order_id} ---")
        for line in self._order_lines:
            print(f"- {line._quantity}x {line._product._name} (@ ${line._product._price:.2f}): ${line.calculate_subtotal():.2f}")
        print(f"Total: ${self.calculate_total():.2f}\n")