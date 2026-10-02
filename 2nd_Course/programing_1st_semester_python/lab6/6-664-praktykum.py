def sort_string(s):
    return ''.join(sorted(s, key=str.lower))

print(sort_string(input()))
