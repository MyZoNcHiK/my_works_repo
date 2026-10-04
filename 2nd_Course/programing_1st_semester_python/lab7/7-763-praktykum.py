number = input()

with open("input.txt", "r") as file:
    if number in file.read().split():
        print("Є")
    else:
        print("Нема")
