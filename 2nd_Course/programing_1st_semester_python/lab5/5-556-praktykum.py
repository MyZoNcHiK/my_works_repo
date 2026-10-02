n = int(input())

synonyms = {}

for i in range(n):
    word1, word2 = input().split()
    synonyms[word1] = word2
    synonyms[word2] = word1

word = input()

print(synonyms[word])
