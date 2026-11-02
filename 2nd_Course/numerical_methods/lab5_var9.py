import math


def f(x):
    return math.exp(-x) - x


def df(x):
    return -math.exp(-x) - 1


eps = 1e-6

a = 0
b = 1

# Метод бісекції
it = 0
left, right = a, b

while right - left > eps:
    c = (left + right) / 2

    if f(left) * f(c) < 0:
        right = c
    else:
        left = c

    it += 1

x_bis = (left + right) / 2

# Метод хорд
it2 = 0
left, right = a, b

while True:
    x = (left * f(right) - right * f(left)) / (f(right) - f(left))

    if abs(f(x)) < eps:
        break

    if f(left) * f(x) < 0:
        right = x
    else:
        left = x

    it2 += 1

x_chord = x

# Метод Ріддерса
it3 = 0
left, right = a, b

while True:
    c = (left + right) / 2

    d = math.sqrt(f(c) ** 2 - f(left) * f(right))

    x = c + (c - left) * math.copysign(1, f(left) - f(right)) * f(c) / d

    if abs(f(x)) < eps:
        break

    if f(left) * f(x) < 0:
        right = x
    else:
        left = x

    it3 += 1

x_ridder = x

# Метод Ньютона
it4 = 0
x = 0.5

while True:
    x_new = x - f(x) / df(x)

    if abs(x_new - x) < eps:
        break

    x = x_new
    it4 += 1

x_newton = x_new

print("Бісекція")
print("x =", x_bis)
print("ітерацій =", it)

print("\nХорд")
print("x =", x_chord)
print("ітерацій =", it2)

print("\nРіддерса")
print("x =", x_ridder)
print("ітерацій =", it3)

print("\nНьютона")
print("x =", x_newton)
print("ітерацій =", it4)
