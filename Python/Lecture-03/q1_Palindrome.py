# Check whether the word is palindrome or not...

user_word = input("Enter any word : ")

reverse_word = ''.join(reversed(user_word))

if(user_word == reverse_word):
    print(f"{user_word} is a palindrome")
else:
    print(f"{user_word} is not a palindrome")