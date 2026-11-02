import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4, 5], dtype=float)

a_true = 2.3
b_true = -0.3

np.random.seed(42)

eps = np.random.uniform(-0.25, 0.25, len(x))

y = a_true * x + b_true + eps

n = len(x)

a = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / \
    (n * np.sum(x ** 2) - np.sum(x) ** 2)

b = (np.sum(y) - a * np.sum(x)) / n

y_hat = a * x + b

r = y - y_hat

r2 = 1 - np.sum(r ** 2) / np.sum((y - np.mean(y)) ** 2)

print("a =", a)
print("b =", b)

print("\ny =", y)

print("\ny_hat =", y_hat)

print("\nr =", r)

print("\nR² =", r2)

plt.scatter(x, y, label="Дані")
plt.plot(x, y_hat, "r", label="Лінійна апроксимація")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()

plt.show()
