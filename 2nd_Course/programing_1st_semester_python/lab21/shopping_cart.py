class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)
        print("Товар", item, "додано до кошика.")

    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
            print("Товар", item, "видалено з кошика.")
        else:
            print("Товар",item, "не знайдено в кошику.")

    def show_items(self):
        print("Товари в кошику:", self.__items)

    def __clear_cart(self):
        self.__items.clear()

    def clear_cart(self):
        self.__clear_cart()
        print("Кошик очищено.")

    def get_item_count(self):
        return len(self.__items)


cart = ShoppingCart()

cart.add_item("Хліб")
cart.add_item("Black 250ml")
cart.add_item("Банани")

cart.show_items()

print("Кількість товарів:", cart.get_item_count())

cart.remove_item("Хліб")
cart.show_items()

try:
    print(cart.__items)
except AttributeError as error:
    print("Помилка:", error)

try:
    cart.__clear_cart()
except AttributeError as error:
    print("Помилка:", error)

#cart.__items.append("Булочка")

cart._ShoppingCart__items.append("Булочка")
cart.show_items()

cart.clear_cart()
cart.show_items()
