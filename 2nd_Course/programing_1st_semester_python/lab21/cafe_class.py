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

