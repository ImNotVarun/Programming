class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, quantity, price_per_unit):
        self.items.append({
            "name": item_name,
            "quantity": quantity,
            "price": price_per_unit
        })

    def calculate_total(self):
        total = sum(item["quantity"] * item["price"] for item in self.items)
        return total

    def print_receipt(self):
        for item in self.items:
            print(f"{item['name']}: {item['quantity']} x ${item['price']}")
        print(f"Total: ${self.calculate_total()}")

# Example usage:
cart = ShoppingCart()
cart.add_item("Apple", 5, 1.5)
cart.add_item("Banana", 3, 0.75)
cart.add_item("Orange", 2, 2.0)
print(f"Total cost: ${cart.calculate_total()}")
cart.print_receipt()