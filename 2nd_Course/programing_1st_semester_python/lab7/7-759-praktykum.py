def sum_in_file(file):
    sum = 0
    for line in file:
        sum += int(line)
    return str(sum)
with open("input.txt", "r") as file:
    print(sum_in_file(file))

