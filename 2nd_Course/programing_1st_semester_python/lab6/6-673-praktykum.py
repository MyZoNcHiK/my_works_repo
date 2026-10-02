def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

s1 = input()
s2 = input()

print(is_anagram(s1, s2))
