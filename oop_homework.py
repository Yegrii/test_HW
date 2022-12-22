
# Products and Carts
#
# Product
# This class represents goods available to purchase in the store.
#
# Each product instance should have next attributes:
# name - a product title (e.g. "apple", "juice")
# price - a price for a single product unit (e.g. 36.55)
# unit - a size of a single product's unit (e.g. 1, 0.500, 12)
# Product class should implement get_total method to calculate price for a specified quantity of a product.
# Quantity arguments is something you can think about as "total number of product's units".
# It is of a numeric type (int or float) and it may be omitted.
# In case argument hasn't been passed just consider it is equal to unit attribute value.
#
# Product should be initialized with all required data, no defaults.


class Product:
    # функція ініціалізації
    def __init__(self, name, price, unit):
        self.name = name
        self.price = price
        self.unit = unit

    def __eq__(self, other):
        # функція для порівняння двох об'єктів
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'

    def __hash__(self):
        return hash(self.name)

    # функція для обчислення загальної суми
    def get_total(self, quantity=None):
        if quantity is None:
            quantity = self.unit
            return round(self.price * quantity, 2)
        else:
            return f'Your total is: {self.price * quantity} UAH'

apple = Product('apple', 36.55, 1)
juice = Product('juice', 53.80, 0.9)
milk = Product('milk', 47.90, 0.85)
water = Product('water', 12.50, 1.5)
bread_half = Product('bread', 21.75, 0.5)
bread_whole = Product('bread', 43.50, 1)
cheese = Product('cheese', 312.00, 1)
butter = Product('butter', 72.40, 0.25)
meat = Product('meat', 255.00, 1)

print(butter.get_total(4))