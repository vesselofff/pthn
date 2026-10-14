class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            self._price = 0
        else:
            self._price = value


class Order:
    def __init__(self):
        self._products = []

    def add_product(self, product: Product):
        self._products.append(product)

    def remove_product(self, product: Product):
        if product in self._products:
            self._products.remove(product)

    @property
    def total_price(self) -> float:
        return sum(p.price for p in self._products)



book = Product("Book", 10)
pen = Product("Pen", 2)
order = Order()
order.add_product(book)
order.add_product(pen)
print(f"Общая стоимость: {order.total_price}")  # 12
