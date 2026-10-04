with open("input.txt", "r") as file:
    text = list(map(int, file.read().split()))
with open("output.txt", "w") as file:
    file.write(str(text[0]+text[1]) + "\n")

