import numpy as np

A = np.array([
    [4, -1, 0],
    [-1, 4, -1],
    [0, -1, 4]
], dtype=float)

b = np.array([4, 4, 4], dtype=float)

x = np.array([1.0, 1.0, 1.0])

for k in range(10):
    x_new = np.zeros(3)

    x_new[0] = (4 + x[1]) / 4
    x_new[1] = (4 + x[0] + x[2]) / 4
    x_new[2] = (4 + x[1]) / 4

    r = A @ x_new - b

    print(f"Ітерація {k + 1}")
    print("x =", x_new)
    print("r =", r)
    print("||r|| =", np.linalg.norm(r))
    print()

    if np.linalg.norm(r) < 1e-6:
        break

    x = x_new
