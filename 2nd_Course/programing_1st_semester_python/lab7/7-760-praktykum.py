def sum_in_file(file):
    sum = 0
    count = 0
    for line in file:
        count += 1
        sum += float(line)
    return str(sum/count)

with open("input.txt", "r") as file:
    print(sum_in_file(file))
