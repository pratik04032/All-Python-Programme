class ReceiptCalculator:
    def __init__(self):
        self.items = []  # List to store the items
        self.tax_rate = 0.07  # Sales tax rate (7%)

    def add_item(self, name, price, quantity):
        item = {
            'name': name,
            'price': price,
            'quantity': quantity,
            'total': price * quantity
        }
        self.items.append(item)

    def calculate_subtotal(self):
        subtotal = sum(item['total'] for item in self.items)
        return subtotal

    def calculate_tax(self, subtotal):
        return subtotal * self.tax_rate

    def calculate_total(self, subtotal, tax):
        return subtotal + tax

    def print_receipt(self):
        print("\nReceipt:")
        print("=" * 30)
        print("{:<15} {:<7} {:<7} {:<10}".format("Item", "Price", "Qty", "Total"))

        for item in self.items:
            print("{:<15} ${:<7.2f} {:<7} ${:<10.2f}".format(item['name'], item['price'], item['quantity'], item['total']))

        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax(subtotal)
        total = self.calculate_total(subtotal, tax)

        print("=" * 30)
        print("Subtotal: ${:.2f}".format(subtotal))
        print("Tax (7%): ${:.2f}".format(tax))
        print("Total: ${:.2f}".format(total))
        print("=" * 30)

    def run(self):
        while True:
            name = input("Enter item name (or 'done' to finish): ")
            if name.lower() == 'done':
                break

            price = float(input(f"Enter price for {name}: $"))
            quantity = int(input(f"Enter quantity for {name}: "))
            self.add_item(name, price, quantity)

        self.print_receipt()

# Run the Receipt Calculator
if __name__ == "__main__":
    calculator = ReceiptCalculator()
    calculator.run()
