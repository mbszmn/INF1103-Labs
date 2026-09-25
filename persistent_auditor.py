import os

FILENAME = "inventory.txt"

def load_inventory():
    if not os.path.exists(FILENAME):
        return 0, []

    try:
        with open(FILENAME, "r") as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
            if not lines:
                return 0, []
            
            inventory_total = int(lines[0])
            history = []
            if len(lines) > 1 and lines[1]:
                history = [int(val) for val in lines[1].split(",")]
                
            return inventory_total, history
    except (ValueError, FileNotFoundError):
        return 0, []

# Define a function to handle input from the user, validate it and produce a clean result.
def get_valid_input():

    user_input = input("Enter stock quantity (or type 'quit' to exit): ").strip()

    # Result 1: if user quits, it returns quit
    if user_input.lower() == 'quit':
        return "quit"

	# Result 2: if user enters an invalid input, program returns None 
	# Reject negative numbers
    if user_input.startswith('-') and user_input[1:].isdigit():
        print("Error: Negative numbers are not allowed.")
        return None

	# Results 3: if user enters a valid integer, program returns the value
	# Accept stock values as integers and update running total
    elif user_input.isdigit():
        return int(user_input)

    else: 
        print("Error: Invalid entry. Enter a valid integer or type 'quit'.")
        return None


# Define a function to calculate two amounts together and return the result.
def process_delivery(current_total, new_value):
    return current_total + new_value

# Define a function that takes the delivery amount, calculates the tax on it, and returns the tax.
def calculate_tax(amount):
    return amount * 0.1 # tax is 10% of the specific delivery

# Define a function that takes total units and no. of failed attempts, and prints a final summary.
def generate_report(total_units, failed_attempts):
    print("\n--- Final Report ---")
    print(f"Total Units Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


def main():
    inventory_total, transaction_history = load_inventory()
    failed_attempts = 0
    processed_deliveries = 0

    print(f"Loaded existing inventory total: {inventory_total}")
    print(f"Loaded transaction history: {transaction_history}\n")

    while True:
        response = get_valid_input()

        if response == "quit":
            print("Exiting the program")
            break

        elif response is None:
            failed_attempts += 1

        else:
            inventory_total = process_delivery(inventory_total, response)
            transaction_history.append(response)  # Appending to memory list
            tax = calculate_tax(response)
            processed_deliveries += 1

            print(f"Delivery processed: {response} units (Tax: ${tax:.2f})")
            print(f"Total Current Inventory: {inventory_total} units\n")

            if inventory_total > 500:
                print("Overstock Alert: Total inventory exceeds 500 units. Terminating audit.")
                break

    generate_report(inventory_total, failed_attempts)

if __name__ == "__main__":
    main()