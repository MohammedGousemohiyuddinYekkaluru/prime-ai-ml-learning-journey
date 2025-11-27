# Write a program that takes a string from the user and prints the number of spaces in the string

let_string = input("Enter a string: ")
count = 0

for letter in let_string:
    if letter == " ":
        count += 1

print(f"Number of spaces : {count}")
