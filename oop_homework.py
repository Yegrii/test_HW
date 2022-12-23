
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
            return f'Total:\n Product: {self.name}\n quantity: {quantity}\n price: {self.price * quantity} UAH'


# Shopping Cart
# This class represents the container for the products.
# It's main responsibility is to store information about the purchases and their amount (quantities).
#
# Each cart instance should store data about Product objects in it and corresponding quantity value for each individual product.
#
# ShoppingCart should implement add_product method to put a specified quantity into a cart.quantity argument is optional,
# if omitted just uses Product.unit value instead.
#
# ShoppingCart should implement get_total method to calculate the total price for the entire cart contents.


class ShoppingCart:
    pass