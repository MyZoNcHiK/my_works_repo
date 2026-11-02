import numpy as np


def F(x):
    return np.array([
        np.exp(x[0]) - x[1] - 2,
        x[0]**2 + x[1]**2 - 3
    ])


def J(x):
    return np.array([
        [np.exp(x[0]), -1],
        [2 * x[0], 2 * x[1]]
    ])


eps = 1e-6
x = np.array([0.5, 1.0])

k = 0

while True:
    f = F(x)

    dx = np.linalg.solve(J(x), -f)

    print(f"Ітерація {k}")
    print("x =", x)
    print("F(x) =", f)
    print("||F|| =", np.linalg.norm(f))
    print()

    if np.linalg.norm(f) < eps or np.linalg.norm(dx) < eps:
        break

    x = x + dx
    k += 1

print("Розв'язок:")
print(x)

