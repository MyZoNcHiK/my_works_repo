numbers = list(map(int, input().split()))
result = []

for number in numbers:
    if number % 2 != 0:
        result.append(number)

print(result)
