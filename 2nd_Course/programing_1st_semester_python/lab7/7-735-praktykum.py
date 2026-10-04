with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
with open("output.txt", "w") as output_file:
    output_file.writelines(lines[::-1])
