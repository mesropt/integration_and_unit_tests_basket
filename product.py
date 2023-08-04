class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}. {self.description}"

# table_1 = Product('Table', 500, 'made from oak')