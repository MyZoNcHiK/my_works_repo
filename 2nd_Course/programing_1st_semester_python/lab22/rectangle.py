class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__length = length

    def set_length(self, length):
        if length > 0:
            self.__length = length
        else:
            raise ValueError("Довжина повинна бути більшою за 0")

    def get_length(self):
        return self.__length

    def set_width(self, width):
        if width > 0:
            self.__width = width
        else:
            raise ValueError("Ширина повинна бути більшою за 0")

    def get_width(self):
        return self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def area(self):
        return self.__length * self.__width

    @staticmethod
    def description():
        return "Rectangle — клас для роботи з прямокутником."

print(Rectangle.description())

rectangle = Rectangle(10, 5)

print("Довжина:", rectangle.get_length())
print("Ширина:", rectangle.get_width())
print("Периметр:", rectangle.perimeter())
print("Площа:", rectangle.area())

rectangle.set_length(8)
rectangle.set_width(4)

print("\nПісля зміни розмірів:")
print("Довжина:", rectangle.get_length())
print("Ширина:", rectangle.get_width())
print("Периметр:", rectangle.perimeter())
print("Площа:", rectangle.area())

