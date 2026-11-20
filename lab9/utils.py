import csv
from product import ProductFactory
from inventory import Inventory
from supplier import Supplier

# Keep asking the user until they enter a valid number greater than zero
def get_positive_float(prompt: str) -> float:
    while True:
        try:
            # Try converting user input text into a float
            value = float(input(prompt))
            # Check that the number is strictly positive
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            # Handle non-numeric text without crashing
            print("Please enter a valid number, e.g. 12.50")


# Load products from a CSV file into an Inventory while skipping invalid rows
def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    try:
        # Try opening the CSV file
        file = open(path, newline="")
    except FileNotFoundError:
        # Handle a missing file gracefully without crashing
        print(f"Products file not found: {path}")
    else:
        # Only runs if the file opened without errors
        with file:
            reader = csv.reader(file)
            # Skip the header row safely
            next(reader, None)
            loaded = 0

            for row in reader:
                # Skip completely empty lines
                if not row:
                    continue
                try:
                    # Clean extra spaces from each column in the row
                    product_type, product_id, name, price_str, stock_str = [cell.strip() for cell in row]
                    # Convert text values to numbers (may raise ValueError)
                    price = float(price_str)
                    stock_quantity = int(stock_str)
                    # Create product via factory (may raise ValueError for bad type/values)
                    product = ProductFactory.create(
                        product_type, product_id, name, price, stock_quantity, supplier
                    )
                    inventory.add_product(product)
                    loaded += 1
                except ValueError as err:
                    # Report the bad row and keep loading the remaining rows
                    print(f"Skipping invalid row {row}: {err}")

            print(f"{loaded} products loaded.")
    finally:
        # Always runs whether the file was found or not
        print("Load attempt finished.")