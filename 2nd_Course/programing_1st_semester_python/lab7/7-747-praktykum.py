from random import randint

with open("input.txt", "r") as file:
    lines = file.readlines()
    r = randint(0,len(lines)-1)
    print(lines[r])
