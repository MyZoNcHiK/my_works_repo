n = int(input())

count = 0
k = 1

while count < n:
    for i in range(k):
        if count < n:
            print(k, end=" ")
            count += 1
    k += 1
print()

