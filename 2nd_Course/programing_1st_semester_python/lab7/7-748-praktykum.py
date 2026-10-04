from random import randint, sample

with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    n = randint(1, len(lines))
    result = sample(lines, n)
    for word in result:
        print(word)
