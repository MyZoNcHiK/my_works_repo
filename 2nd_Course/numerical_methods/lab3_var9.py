import numpy as np

A = np.array([
    [1, -2, 3],
    [2, 1, 2],
    [4, -1, 1]
], dtype=float)

b = np.array([1, 5, 6], dtype=float)

n = len(A)

L = np.eye(n)
U = np.zeros((n, n))

for i in range(n):
    for j in range(i, n):
        U[i][j] = A[i][j]
        for k in range(i):
            U[i][j] -= L[i][k] * U[k][j]

    for j in range(i + 1, n):
        L[j][i] = A[j][i]
        for k in range(i):
            L[j][i] -= L[j][k] * U[k][i]

        L[j][i] /= U[i][i]

y = np.zeros(n)

for i in range(n):
    y[i] = b[i]
    for j in range(i):
        y[i] -= L[i][j] * y[j]

x = np.zeros(n)

for i in range(n - 1, -1, -1):
    x[i] = y[i]
    for j in range(i + 1, n):
        x[i] -= U[i][j] * x[j]

    x[i] /= U[i][i]

r = A @ x - b

print("L:")
print(L)

print("\nU:")
print(U)

print("\nLU:")
print(L @ U)

print("\nx:")
print(x)

print("\nr:")
print(r)

print("\n||r||:")
print(np.linalg.norm(r))
