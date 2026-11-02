import numpy as np
import math


def phi1(x1, x2):
    return math.cos(x2) + 1


def phi2(x1, x2):
    return math.sqrt(x1)


def f1(x1, x2):
    return x1 - math.cos(x2) - 1


def f2(x1, x2):
    return x2 - math.sqrt(x1)


eps = 1e-6

x = np.array([0.5, 0.5])

k = 0

while True:
    x_new = np.array([
        phi1(x[0], x[1]),
        phi2(x[0], x[1])
    ])

    r = np.array([
        f1(x_new[0], x_new[1]),
        f2(x_new[0], x_new[1])
    ])

    print(f"Ітерація {k}")
    print("x =", x_new)
    print("r =", r)
    print("||r|| =", np.linalg.norm(r))
    print()

    if np.linalg.norm(x_new - x) < eps:
        break

    x = x_new
    k += 1

print("Розв'язок:")
print(x_new)
