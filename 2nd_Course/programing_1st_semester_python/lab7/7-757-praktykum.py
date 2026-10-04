with open("input.txt", "r") as file:
    lines = file.readlines()[-3:]    
    for line in lines:
        print(line.rstrip())
