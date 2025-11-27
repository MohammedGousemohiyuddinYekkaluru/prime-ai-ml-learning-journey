# Given list of words, Create a dictionary that maps each word to its length...

words = ["apple", "banana", "kiwi", "cherry", "mango"]

words_dict = {}

for word in words:
   words_dict[word] = len(word)

print(words_dict)
