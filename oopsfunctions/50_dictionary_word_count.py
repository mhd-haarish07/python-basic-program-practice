# 50. Dictionary Basics - Word Count
text = "apple banana apple orange banana apple"
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)
