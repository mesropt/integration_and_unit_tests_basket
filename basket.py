class Basket:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_total(self):
        total = sum(product.price for product in self.products)
        return total

    def __str__(self):
        product_list = "\n".join(str(product) for product in self.products)
        return f"Basket:\n{product_list}\nTotal: ${self.get_total():.2f}"

# basket = Basket()
# product_1 = Product("Table 1", 300, 'Made from birch')
# product_2 = Product("Table 2", 600, 'Made from pine')
#
# basket.add_product(product_1)
# basket.add_product(product_2)

# basket = Basket()
# print(basket)
