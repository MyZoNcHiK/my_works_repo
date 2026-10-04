with open("input.txt", "r") as file:
    words = file.read().split()
    unique_list = []
    for word in words:
        if word not in unique_list:
            unique_list.append(word)
    print(unique_list)        

