with open("input.txt", "r") as file:
    date = file.read().strip()

while len(date) > 1:
    date = str(sum(map(int, date)))

with open("output.txt", "w") as file:
    file.write(date + "\n")
