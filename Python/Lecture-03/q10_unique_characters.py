# Ask the user for a string and print: 1)All unique characters and 2)The count of unique characters

user = input("Enter a string : ")

unique_chars = set(user)

print(f"\nUnique Characters: ")
for char in unique_chars:
    print(char)

print(f"\n Total unique characters: {len(unique_chars)}")