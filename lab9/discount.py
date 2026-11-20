from abc import ABC, abstractmethod

# Abstract base class that defines the common interface for all discount strategies
class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        # Take the original order total and return the discounted total
        pass


# Strategy 1: Applies no discount and returns the original total
class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total


# Strategy 2: Takes a percentage off the total (e.g. 10 means 10% off)
class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float):
        # Store the discount percentage
        self.percent = percent

    def apply(self, total: float) -> float:
        # Subtract the percentage from the total
        return total * (1 - self.percent / 100)


# Strategy 3: Subtracts a fixed amount if the total meets a minimum threshold
class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, amount: float):
        # Store the minimum spend needed and the fixed discount amount
        self.threshold = threshold
        self.amount = amount

    def apply(self, total: float) -> float:
        # Apply the discount only if the total reaches the threshold
        if total >= self.threshold:
            return total - self.amount
        return total


# Strategy 4 (Extension): Applies a 5% student discount without modifying Order
class StudentDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        # Return the total after taking 5% off
        return total * 0.95