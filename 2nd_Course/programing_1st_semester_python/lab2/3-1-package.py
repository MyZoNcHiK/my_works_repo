try:
    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))

    assert a >= 0
    assert b >= 0

    s = a + b
    r = a / b

except AssertionError:
    print("Помилка: число не може бути від'ємним")

except ZeroDivisionError:
    print("Помилка: ділення на нуль")

else:
    print("Сума:", s)
    print("Частка:", r)

finally:
    print("Програму завершено")
