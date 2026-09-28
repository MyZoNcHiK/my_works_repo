n = int(input())

factorial = 1
s = 0

for i in range(1, n + 1):
    factorial *= i
    s += factorial

print(s)
