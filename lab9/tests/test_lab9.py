import os
import tempfile
import unittest
from unittest.mock import patch

from supplier import Supplier
from product import ProductFactory, PhysicalProduct, DigitalProduct
from inventory import Inventory
from order import Order, OrderLine
from discount import NoDiscount, PercentageDiscount, BulkDiscount, StudentDiscount
from utils import get_positive_float, load_products


class TestLab9DesignPatternsAndValidation(unittest.TestCase):
    def setUp(self):
        # Create a reusable supplier and sample product before each test
        self.supplier = Supplier("SUP01", "Acme Supply", "sales@acme.com")
        self.item = ProductFactory.create("physical", "P100", "Monitor", 125.0, 10, self.supplier)

    # --- Section 2: Strategy Pattern Tests ---
    def test_order_default_no_discount(self):
        # Order with no discount given should use NoDiscount
        order = Order("O1")
        order.add_line(self.item, 2)  # Subtotal = 250.0
        self.assertEqual(order.calculate_total(), 250.0)

    def test_order_bulk_and_percentage_discount_switch(self):
        # Order should calculate BulkDiscount and allow changing strategy via set_discount
        order = Order("O2", BulkDiscount(200, 20))
        order.add_line(self.item, 2)  # Subtotal = 250.0
        self.assertEqual(order.calculate_total(), 230.0)

        # Change discount strategy at runtime
        order.set_discount(PercentageDiscount(10))
        self.assertEqual(order.calculate_total(), 225.0)

    def test_student_discount_extension(self):
        # New StudentDiscount strategy should work without modifying Order
        order = Order("O3", StudentDiscount())
        order.add_line(self.item, 2)  # Subtotal = 250.0
        self.assertAlmostEqual(order.calculate_total(), 237.5)

    # --- Section 3: Factory Pattern Tests ---
    def test_product_factory_creates_subclasses(self):
        # Factory should return PhysicalProduct and DigitalProduct instances
        phys = ProductFactory.create("physical", "P001", "Desk", 100.0, 5, self.supplier)
        digi = ProductFactory.create("digital", "D001", "Ebook", 20.0, 50, self.supplier)
        self.assertIsInstance(phys, PhysicalProduct)
        self.assertIsInstance(digi, DigitalProduct)

    def test_product_factory_unknown_type_raises_value_error(self):
        # Factory should raise ValueError for unsupported product types
        with self.assertRaises(ValueError):
            ProductFactory.create("service", "S001", "Setup", 30.0, 5, self.supplier)

    # --- Section 4: Validation Tests ---
    def test_invalid_product_price_and_stock_rejected(self):
        # Zero or negative price must raise ValueError
        with self.assertRaises(ValueError):
            ProductFactory.create("physical", "P002", "BadPrice", 0, 5, self.supplier)
        with self.assertRaises(ValueError):
            ProductFactory.create("physical", "P003", "NegPrice", -10.0, 5, self.supplier)

        # Negative stock must raise ValueError
        with self.assertRaises(ValueError):
            ProductFactory.create("physical", "P004", "NegStock", 10.0, -1, self.supplier)

    def test_invalid_order_line_quantity_rejected(self):
        # Zero or negative order quantity must raise ValueError
        with self.assertRaises(ValueError):
            OrderLine(self.item, 0)
        with self.assertRaises(ValueError):
            OrderLine(self.item, -3)

    # --- Section 5: Exception Handling Tests ---
    @patch("builtins.input", side_effect=["abc", "-5", "12.50"])
    def test_get_positive_float_reprompts_until_valid(self, mock_input):
        # Helper should skip invalid text and negative numbers, then return 12.5
        result = get_positive_float("Enter price: ")
        self.assertEqual(result, 12.5)
        self.assertEqual(mock_input.call_count, 3)

    def test_load_products_missing_file_handled_gracefully(self):
        # Missing file should not crash the program
        inv = Inventory()
        load_products("non_existent_file.csv", inv, self.supplier)
        self.assertEqual(len(inv.products), 0)

    def test_load_products_skips_bad_rows_and_loads_valid_ones(self):
        # Valid rows should load while bad type and non-numeric price rows are skipped
        csv_content = (
            "product_type, product_id,name, price, stock_quantity\n"
            "physical, P001, Desk Lamp, 25.00,10\n"
            "digital, D001, Photo Editor, 49.90,100\n"
            "service, S001, Installation, 30.00,5\n"
            "physical, P002, Office Chair, abc, 3\n"
            "physical, P003, Monitor Stand, 39.50,7\n"
        )
        # Create a temporary CSV file for isolated testing
        with tempfile.NamedTemporaryFile("w", delete=False, suffix=".csv", newline="") as tmp:
            tmp.write(csv_content)
            tmp_path = tmp.name

        try:
            inv = Inventory()
            load_products(tmp_path, inv, self.supplier)
            # Only P001, D001, and P003 should be loaded
            self.assertEqual(len(inv.products), 3)
            self.assertIn("P001", inv.products)
            self.assertIn("D001", inv.products)
            self.assertIn("P003", inv.products)
        finally:
            os.remove(tmp_path)


if __name__ == "__main__":
    unittest.main()