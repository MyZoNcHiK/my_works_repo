class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def get_max_speed(self):
        return self.max_speed

    def move(self):
        print("Транспорт рухається кудись, чомусь і нащось")


class WaterVehicle(Vehicle):
    def __init__(self, max_speed, displacement):
        super().__init__(max_speed)
        self.displacement = displacement

    def get_displacement(self):
        return self.displacement

class Ship(WaterVehicle):
    def __init__(self, max_speed, displacement, ship_type):
        super().__init__(max_speed, displacement)
        self.ship_type = ship_type

    def get_ship_type(self):
        return self.ship_type

ship = Ship(60, 15000, "Вантажний корабель")

print("Максимальна швидкість:", ship.get_max_speed(), "км/год")
print("Водотоннажність:", ship.get_displacement(), "тонн")
print("Тип судна:", ship.get_ship_type())
