class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def set_hour(self, hour):
        if 0 <= hour <= 23:
            self.__hour = hour
        else:
            raise ValueError("Година має бути від 0 до 23")

    def get_hour(self):
        return self.__hour

    def set_minute(self, minute):
        if 0 <= minute <= 59:
            self.__minute = minute
        else:
            raise ValueError("Хвилина має бути від 0 до 59")

    def get_minute(self):
        return self.__minute

    def set_second(self, second):
        if 0 <= second <= 59:
            self.__second = second
        else:
            raise ValueError("Секунда має бути від 0 до 59")

    def get_second(self):
        return self.__second

    def add_second(self):
        self.__second += 1
        if self.__second == 60:
            self.__second = 0
            self.add_minute()

    def add_minute(self):
        self.__minute += 1
        if self.__minute == 60:
            self.__minute = 0
            self.add_hour()

    def add_hour(self):
        self.__hour += 1
        if self.__hour == 24:
            self.__hour = 0

    def show_time(self):
        print(f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}")

    @staticmethod
    def is_valid_time(hour, minute, second):
        return (
            0 <= hour <= 23
            and 0 <= minute <= 59
            and 0 <= second <= 59
        )


time1 = Time(12, 30, 58)
time1.show_time()

time1.add_second()
time1.show_time()

time1.add_minute()
time1.show_time()

time1.add_hour()
time1.show_time()

print(time1.get_hour())
print(time1.get_minute())
print(time1.get_second())

time1.set_hour(20)
time1.set_minute(45)
time1.set_second(10)
time1.show_time()

print(Time.is_valid_time(23, 59, 59))
print(Time.is_valid_time(25, 10, 10))

