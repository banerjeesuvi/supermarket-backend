from Checkout import Checkout
from Product import Product


def main():
    # Pricing rules
    pricing_rules = {
        'A': Product('A', 50, 3, 130),
        'B': Product('B', 30, 2, 45),
        'C': Product('C', 20),
        'D': Product('D', 15)
    }

    checkout = Checkout(pricing_rules)

    items = "AAA"
    for item in items:
        checkout.add_item(item)

    # Calculate the total price
    total = checkout.calculate_total()
    print(f"Total price for items '{items}' is: {total}")

if __name__ == "__main__":
    main()