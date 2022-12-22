
Products and Carts

Product
This class represents goods available to purchase in the store.

Each product instance should have next attributes:
name - a product title (e.g. "apple", "juice")
price - a price for a single product unit (e.g. 36.55)
unit - a size of a single product's unit (e.g. 1, 0.500, 12)
Product class should implement get_total method to calculate price for a specified quantity of a product.
Quantity arguments is something you can think about as "total number of product's units".
It is of a numeric type (int or float) and it may be omitted.
In case argument hasn't been passed just consider it is equal to unit attribute value.