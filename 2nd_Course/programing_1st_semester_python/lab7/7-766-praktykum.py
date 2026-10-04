def write_to_file(file):
    n = int(input())
    for i in range(n):
        university = input()
        rate = int(input())
        file.write(university + ", " + str(rate) + "\n")

with open(input(), "a") as file:
    write_to_file(file)
