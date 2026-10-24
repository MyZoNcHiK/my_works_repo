#починаючи здавати треба буде сказати що маємо клас, з двома приватними полями як вказано в завданні
#та приватним методом
#і бажано показати курсором
class Order:
    def __init__(self, customer, products, quantities):
        self.customer = customer
        self.__products = products #приватне поле 1
        self.__quantities = quantities #приватне поле 2

    def __calculate_total(self): #приватний метод який рахує загальну суму замовлення(можна так і казати щоб переконати що знаєш що робить код
        total = 0
        for i in range(len(self.__products)):
            total += self.__products[i]["price"] * self.__quantities[i]
        return total

    def show_info(self): #можна сказати "тут звичайні методи для виведення" і далі цю функцію не згадувати навіть
        print(f"Замовник: {self.customer}")
        print("Товари в замовленні:")

        for i in range(len(self.__products)):
            product = self.__products[i]
            quantity = self.__quantities[i]
            cost = product["price"] * quantity
            print(
                f"{product['name']}: {quantity} шт. × "
                f"{product['price']} грн = {cost} грн"
                )
        print(f"Загальна вартість: {self.__calculate_total()} грн")

    def get_total(self): #це гетер для безпечного доступу до приватного методу
        return self.__calculate_total()

product1 = {"name": "Ноутбук", "price": 25000}
product2 = {"name": "Миша", "price": 800}
product3 = {"name": "Клавіатура", "price": 1500}
#тут створюються екземпляри класу
order1 = Order("Андрій", [product1, product2], [1, 2])
order2 = Order("Олена", [product2, product3], [1, 1])

#тут використовуються базові методи 
order1.show_info()
print()
order2.show_info()
print(order1.get_total())

# a це спроби напряму звернутися до приватних полів в блоці try-except бо викликають помилку
try:
    print(order1.__products)
except AttributeError as e:
    print(e)
try:
    print(order1.__calculate_total())
except AttributeError as e:
    print(e)
#доступ до інкапсульованих поля та методу через механізм коригування імен
print(order1._Order__products)
print(order1._Order__calculate_total())

