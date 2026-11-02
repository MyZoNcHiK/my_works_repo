def decorator(cls):
    class Wrapper(cls):
        def show_results(self):
            results = [
                self.first(),
                self.second(),
                self.third()
            ]

            print("Мінімальне значення:", min(results))
            print("Максимальне значення:", max(results))

    return Wrapper

@decorator
class Numbers:
    def first(self):
        return 15

    def second(self):
        return 8

    def third(self):
        return 25


obj = Numbers()

print(obj.first())
print(obj.second())
print(obj.third())

obj.show_results()
