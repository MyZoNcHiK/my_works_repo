try:
    a = int(input("Введіть a: "))
    b = int(input("Введіть b: "))

    result = 1 / (a - b)

    print("Результат:", result)

except ZeroDivisionError:
    print("Помилка: ділення на нуль!")
