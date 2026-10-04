words_count={}
def count_words(file):
    words = file.read().split() 
    for word in words:
        words_count[word] = words_count.get(word, 0) + 1
with open("input.txt", "r") as file:
    count_words(file)
print(words_count)
