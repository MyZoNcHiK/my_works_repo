try:
    a = int(input("Введіть a: "))
    b = int(input("Введіть b: "))

    assert a >= 0
    assert b >= 0

    result = a - b

except ValueError:
    print("Помилка: потрібно ввести ціле число")

except AssertionError:
    print("Помилка: число не може бути від'ємним")

else:
    print("Різниця:", result)

finally:
    print("Програму завершено")
