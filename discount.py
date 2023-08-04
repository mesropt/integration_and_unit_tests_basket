class Discount:
    def __init__(self, condition, amount):
        self.condition = condition
        self.amount = amount

    def apply_discount(self, product):
        if self.condition(product):
            product.price -= self.amount