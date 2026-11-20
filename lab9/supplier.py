# Represents a product supplier
class Supplier:
    def __init__(self, supplier_id: str, name: str, contact_email: str):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_email = contact_email

    def display_information(self) -> None:
        # Print supplier contact details
        print(f"Supplier: {self.name} ({self.supplier_id}) - {self.contact_email}")