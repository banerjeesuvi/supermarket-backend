class Product:
    def __init__(self, name, price, discount_quantity=0, discount_price=0):
        self.name = name
        self.price = price
        self.discount_quantity = discount_quantity
        self.discount_price = discount_price

    def get_price(self, quantity):
        if self.discount_quantity > 0:
            discount_sets = quantity // self.discount_quantity
            remainder = quantity % self.discount_quantity
            return discount_sets * self.discount_price + remainder * self.price
        else:
            return quantity * self.price