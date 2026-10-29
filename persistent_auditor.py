import os

FILENAME = "inventory.txt"

# Persistence: read the information previously saved in the inventory file
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

# Write-back: save the final total and the transaction history list to inventory.txt
def save_inventory(total, history):
    with open(FILENAME, "w") as f:
        f.write(f"{total}\n")
        f.write(",".join(map(str, history)) + "\n")
    print(f"Data successfully saved to {FILENAME}")


def get_valid_input():
    user_input = input("Enter stock quantity (or type 'quit' to exit): ").strip()

    if user_input.lower() == 'quit':
        return "quit"

    if user_input.startswith('-') and user_input[1:].isdigit():
        print("Error: Negative numbers are not allowed.")
        return None
    elif user_input.isdigit():
        return int(user_input)
    else: 
        print("Error: Invalid entry. Enter a valid integer or type 'quit'.")
        return None


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.1


def generate_report(total_units, failed_attempts):
    print("\n--- Final Report ---")
    print(f"Total Units Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


def main():
    # 1. Persistence Load on startup
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
            transaction_history.append(response)  # 2. Track in Python array
            tax = calculate_tax(response)
            processed_deliveries += 1

            print(f"Delivery processed: {response} units (Tax: ${tax:.2f})")
            print(f"Total Current Inventory: {inventory_total} units\n")

            if inventory_total > 500:
                print("Overstock Alert: Total inventory exceeds 500 units. Terminating audit.")
                break

    # 3. Save on exit
    save_inventory(inventory_total, transaction_history)
    generate_report(processed_deliveries, failed_attempts)


if __name__ == "__main__":
    main()

    