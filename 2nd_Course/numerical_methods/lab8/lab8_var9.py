import numpy as np
import matplotlib.pyplot as plt


def fft(x):
    n = len(x)

    if n == 1:
        return x

    even = fft(x[::2])
    odd = fft(x[1::2])

    w = np.exp(-2j * np.pi * np.arange(n // 2) / n)

    return np.concatenate([
        even + w * odd,
        even - w * odd
    ])


N = 512
T = 1

t = np.arange(N) * T / N

x = (1 + 0.7 * np.cos(4 * t)) * np.sin(110 * np.pi * t)

X = fft(x)

X_np = np.fft.fft(x)

error = np.max(np.abs(X - X_np))

f = np.arange(N // 2 + 1) / T

amp = 2 * np.abs(X[:N // 2 + 1]) / N

print("Максимальна різниця FFT:")
print(error)

plt.figure(figsize=(10, 5))
plt.plot(f, amp)
plt.xlabel("Частота, Гц")
plt.ylabel("|X(f)|")
plt.title("Амплітудно-частотна характеристика")
plt.grid()
plt.show()
