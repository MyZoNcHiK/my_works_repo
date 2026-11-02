from datetime import datetime
import time

def decorator(func):
    def wrapper():
        print("Дата:", datetime.now().date())

        start = time.time()
        func()
        end = time.time()

        print("Час виконання:", end - start, "секунд")

    return wrapper

@decorator
def hello():
    print("Виконання функції...")
    time.sleep(2)

hello()
