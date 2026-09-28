s = 0
count = 0

n = int(input())

while n != 0:
    s += n
    count += 1
    n = int(input())

print(s / count)
