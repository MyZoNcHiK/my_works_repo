class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        print(f"Товар: {self.name}")
        print(f"Ціна: {self.price} грн")


class Store:
    def __init__(self, name, product_name, product_price):
        self.name = name
        self.product = Product(product_name, product_price)

    def show_info(self):
        print(f"Магазин: {self.name}")
        self.product.show_info()


class Order:
    def __init__(self, store_name, product_name, product_price, quantity):
        self.store = Store(store_name, product_name, product_price)
        self.product = self.store.product
        self.quantity = quantity

    def total_price(self):
        return self.product.price * self.quantity

    def show_order(self):
        print(f"Магазин: {self.store.name}")
        print(f"Товар: {self.product.name}")
        print(f"Ціна за одиницю: {self.product.price} грн")
        print(f"Кількість: {self.quantity}")
        print(f"Загальна вартість: {self.total_price()} грн")


store1 = Store("ТехноСвіт", "Ноутбук", 25000)
store2 = Store("Комп'ютерний світ", "Мишка", 700)
store3 = Store("ГаджетМаркет", "Клавіатура", 1500)

store1.show_info()
print()
store2.show_info()
print()
store3.show_info()

order1 = Order("ТехноСвіт", "Ноутбук", 25000, 1)
order2 = Order("Комп'ютерний світ", "Мишка", 700, 2)
order3 = Order("ГаджетМаркет", "Клавіатура", 1500, 1)

order1.show_order()
order2.show_order()
order3.show_order()
