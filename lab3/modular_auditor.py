# Initialize the inventory to zero
inventory = 0

# Initialize failed entries counter for reporting
failed_entries = 0  

# Continuous loop asking user to enter a stock quantity until quit
while True:
    user_input = input("Enter stock quantity (or type 'quit' to exit): ").strip()

    if user_input.lower() == 'quit':
        print("Exiting the program")
        break

    # Reject negative numbers
    elif user_input.startswith('-') and user_input[1:].isdigit():
        failed_entries += 1
        print("Error:Negative numbers are not allowed.")

    # Accept stock values as integers and update running total
    elif user_input.isdigit():
        stock_added = int(user_input)
        inventory += stock_added
        print(f"Stock added: {stock_added} units.")
        print(f"Total current inventory: {inventory} units")

        # Overstock alert check
        if inventory > 500:
            print("Overstock Alert: Inventory exceeds 500 units.")
            break

    # Reject invalid string inputs
    else:
        failed_entries += 1
        print("Invalid input. Please enter a valid stock quantity or type 'quit'.")

# Summary on exit
print("\n--- Final Report ---")
print(f"Total Units Processed: {inventory}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")