
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
    # функція ініціалізації
    def __init__(self):
        self.products = {}

    def __str__(self):
        return f'{self.products}'

    def __repr__(self):
        return f'{self.products}'

    def __eq__(self, other):
        # функція для порівняння двох об'єктів
        if not isinstance(other, ShoppingCart):
            return False
        return self.products == other.products

    def __hash__(self):
        return hash(self.products)

    # функція для додавання продукту в корзину
    def add_product(self, product, quantity=None):
        if quantity is None:
            quantity = product.unit
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity
        return f'Product {product.name} added to cart'

    # функція для обчислення загальної суми
    def get_cart_total(self):
        prod = []
        quant = []
        for key, value in self.products.items():
            prod.append(key)
            quant.append(value)
        total = 0
        for i in range(len(prod)):
            total += prod[i].price * quant[i]
        return ''.join(f'Product: {prod[i].name}\n quantity: {quant[i]}\n '
            f'price: {round(prod[i].price * quant[i], 2)} UAH\n' for i in range(len(prod))) + \
            f'Total price: {total} UAH'

# Тестування

# створити продукти
# створити кошик
# додати продукти в кошик
# обчислити загальну суму


if __name__ == '__main__':
    apple = Product('apple', 23.2, 1)
    juice = Product('juice', 49.60, 0.75)
    milk = Product('milk', 53.5, 1)
    bread = Product('bread', 25.5, 1)
    meat = Product('meat', 221.0, 1)
    beans = Product('beans', 45.0, 1)
    sneakers_big = Product('sneakers 3 in 1', 33.45, 1)
    sneakers_small = Product('sneakers', 16.90, 1)


    cart = ShoppingCart()
    cart.add_product(apple, 2)
    cart.add_product(juice, 2)
    cart.add_product(milk, 1)
    cart.add_product(apple, 2)
    cart.add_product(juice, 1)
    cart.add_product(bread, 1)
    cart.add_product(meat, 0.7)
    cart.add_product(beans, 1)
    cart.add_product(sneakers_big, 1)
    cart.add_product(sneakers_small, 3)


    print(cart.get_cart_total())

# Результат
# Product: apple
#     quantity: 4
#     price: 92.8 UAH
# Product: juice
#     quantity: 3
#     price: 148.8 UAH
# Product: milk
#     quantity: 1
#     price: 53.5 UAH
# Product: bread
#     quantity: 1
#     price: 25.5 UAH
# Product: meat
#     quantity: 0.7
#     price: 154.7 UAH
# Product: beans
#     quantity: 1
#     price: 45.0 UAH
# Product: sneakers 3 in 1
#     quantity: 1
#     price: 33.45 UAH
# Product: sneakers
#     quantity: 3
#     price: 50.7 UAH
# Total price: 549.35 UAH
