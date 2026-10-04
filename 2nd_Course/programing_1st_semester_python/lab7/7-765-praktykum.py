n = input()
with open("input.txt", "r") as input_file:
    with open("output.txt", "w") as output_file:
        while s := input_file.read(1):
            if s == n:
                output_file.write("YES\n")
                break
        else:
            output_file.write("NO\n")
             
