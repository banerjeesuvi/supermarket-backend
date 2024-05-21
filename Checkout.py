class Checkout:
    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules
        self.cart = {}

    def add_item(self, item):
        if item in self.cart:
            self.cart[item] += 1
        else:
            self.cart[item] = 1

    def calculate_total(self):
        total = 0
        for item, quantity in self.cart.items():
            product = self.pricing_rules[item]
            total += product.get_price(quantity)
        return total