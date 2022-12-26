
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

    # функція для додавання продукту в кошик
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
        # розумію що мабуть потрібно було зробити так
        # return f'Total price: {round(total, 2)} UAH'

        # але хотілось зробити красивіше
        return ''.join(f'Product: {prod[i].name}\n quantity: {quant[i]}\n '
            f'price: {round(prod[i].price * quant[i], 2)} UAH\n' for i in range(len(prod))) + \
            f'Total price: {round(total, 2)} UAH\n'

    # функція для видалення продукту з кошика
    def delete_product(self, product, prod_quantity=None):
        if prod_quantity is None:
            del self.products[product]
            return print(f'The product is completely removed. {product.name}--DELETED\n')
        else:
            self.products[product] -= prod_quantity
            # скористався print, тому що return нічого не виводить до консолі(поки що не зрозумів чому)
        return print(f'Deleting product:\n {product.name} in quantity {prod_quantity}'
                     f' deleted from cart for the amount of {round(prod_quantity * product.price, 2)} UAH \n')
    # функція для очищення кошика
    def clear_cart(self):
        self.products.clear()
        return 'Cart is empty\n'
    #  функція для видалення об'єкта ShoppingCart
    def delete_cart(self):
        del self.products
        return f'Cart is deleted\n'


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
    maccoffe = Product('MacCoffe', 12.0, 1)
    potato_pink_washed = Product('potato pink washed', 33.45, 1)
    potato_pink = Product('potato pink', 27.99, 1)
    potato_white = Product('potato white', 21.89, 1)


    cart = ShoppingCart()
    cart.add_product(apple, 4)
    cart.add_product(juice, 5)
    cart.add_product(milk, 3)
    cart.add_product(meat, 1.345)
    cart.add_product(beans, 1)
    cart.add_product(sneakers_big)
    cart.add_product(sneakers_small)
    cart.add_product(maccoffe, 4)
    cart.add_product(potato_pink_washed, 1.2)
    cart.add_product(potato_pink, 1.52)
    cart.add_product(potato_white, 1.01)

# видаляється продукт який був доданий в кошик
    cart.delete_product(juice)

# виводиться загальна сума з описом продуктів
    print(cart.get_cart_total())

# видаляється продукт з вказаною кількістю
    cart.delete_product(potato_pink, 0.52)

# видалення всіх продуктів з кошика (робимо чистий кошик)
    print(cart.clear_cart())

# видаляється екземпляр класу ShoppingCart
    print(cart.delete_cart())

# Результат

# видаляється продукт який був доданий в кошик
# the product is completely removed. juice--DELETED

# виводиться загальна сума з описом продуктів
# Product: apple
#  quantity: 4
#  price: 92.8 UAH
# Product: milk
#  quantity: 3
#  price: 160.5 UAH
# Product: meat
#  quantity: 1.345
#  price: 297.25 UAH
# Product: beans
#  quantity: 1
#  price: 45.0 UAH
# Product: sneakers 3 in 1
#  quantity: 1
#  price: 33.45 UAH
# Product: sneakers
#  quantity: 1
#  price: 16.9 UAH
# Product: MacCoffe
#  quantity: 4
#  price: 48.0 UAH
# Product: potato pink washed
#  quantity: 1.2
#  price: 40.14 UAH
# Product: potato pink
#  quantity: 1.52
#  price: 42.54 UAH
# Product: potato white
#  quantity: 1.01
#  price: 22.11 UAH
# Total price: 798.69 UAH

# видаляється екземпляр класу ShoppingCart
# Cart is empty







