words = input().split()

with open("input.txt", "w") as file:
    for word in words:
        file.write(word + "\n")

with open("input.txt", "r") as file:
    print(file.read())
