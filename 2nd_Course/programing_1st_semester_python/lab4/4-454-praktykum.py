numbers = list(map(int, input().split()))

for number in numbers:
    if number % 2 != 0:
        print(number)
