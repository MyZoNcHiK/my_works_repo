class Cafe:
    def __init__(self, cafe_name, cuisine_type):
        self.cafe_name = cafe_name
        self.cuisine_type = cuisine_type
        self.number_of_tables = 0

    def describe_cafe(self):
        print("Назва кафе:", self.cafe_name)
        print("Тип кухні:", self.cuisine_type)

    def open_cafe(self):
        print("Кафе відкрите!")

    def set_number_of_tables(self, number):
        self.number_of_tables = number

    def increment_number_of_tables(self, number):
        self.number_of_tables += number


cafe = Cafe("Зустріч", "Українська кухня")

print(cafe.cafe_name)
print(cafe.cuisine_type)

cafe.describe_cafe()
cafe.open_cafe()

print()

second_cafe = Cafe("Касдак", "Українська кухня")
second_cafe.describe_cafe()

print()

print("Кількість столиків:", cafe.number_of_tables)

cafe.number_of_tables = 10
print("Кількість столиків після зміни:", cafe.number_of_tables)

cafe.set_number_of_tables(15)
print("Кількість столиків після виклику методу:", cafe.number_of_tables)

cafe.increment_number_of_tables(5)
print("Кількість столиків після збільшення:", cafe.number_of_tables)
