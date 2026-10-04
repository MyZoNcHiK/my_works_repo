def print_file():
    with open("input.txt", "r") as file:
        for number, line in enumerate(file, 1):
            print(number, ":", line, end="")

print_file()
