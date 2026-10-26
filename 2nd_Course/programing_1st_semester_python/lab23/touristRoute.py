class TouristRoute:
    def __init__(self, name, country, duration, difficulty):
        self.__name = name
        self.__country = country
        self.__duration = duration
        self.__difficulty = difficulty

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_country(self, country):
        self.__country = country

    def get_country(self):
        return self.__country

    def set_duration(self, duration):
        self.__duration = duration

    def get_duration(self):
        return self.__duration

    def set_difficulty(self, difficulty):
        self.__difficulty = difficulty

    def get_difficulty(self):
        return self.__difficulty

    def show_info(self):
        print(f"Назва: {self.__name}")
        print(f"Країна: {self.__country}")
        print(f"Тривалість: {self.__duration} днів")
        print(f"Складність: {self.__difficulty}")


class ExtremeRouteWithoutSuper(TouristRoute):
    def __init__(self, name, country, duration, difficulty, obstacles):
        TouristRoute.__init__(self, name, country, duration, difficulty)
        self.__obstacles = obstacles

    def set_obstacles(self, obstacles):
        self.__obstacles = obstacles

    def get_obstacles(self):
        return self.__obstacles

    def calculate_cost(self):
        return self.get_duration() * 1000 + self.__obstacles * 500

    def show_info(self):
        TouristRoute.show_info(self)
        print(f"Кількість перешкод: {self.__obstacles}")
        print(f"Вартість: {self.calculate_cost()} грн")


class ExtremeRoute(TouristRoute):
    def __init__(self, name, country, duration, difficulty, obstacles):
        super().__init__(name, country, duration, difficulty)
        self.__obstacles = obstacles

    def set_obstacles(self, obstacles):
        self.__obstacles = obstacles

    def get_obstacles(self):
        return self.__obstacles

    def calculate_cost(self):
        return self.get_duration() * 1000 + self.__obstacles * 500

    def show_info(self):
        super().show_info()
        print(f"Кількість перешкод: {self.__obstacles}")
        print(f"Вартість: {self.calculate_cost()} грн")


route1 = TouristRoute("Карпатський похід", "Україна", 3, "Середня")
print("Звичайний туристичний маршрут:")
route1.show_info()

print()

route2 = ExtremeRouteWithoutSuper("Сходження на Говерлу", "Україна", 2, "Висока", 5)

route2.show_info()

print()

route3 = ExtremeRoute("Гірський трекінг", "Непал", 7, "Висока", 10)
route3.show_info()

print()
print(route3.get_name())
print(route3.get_country())
print(route3.get_duration())
print(route3.get_difficulty())
print(route3.get_obstacles())

route3.set_name("Еверест: базовий табір")
route3.set_country("Непал")
route3.set_duration(8)
route3.set_difficulty("Дуже висока")
route3.set_obstacles(12)

print()
route3.show_info()

