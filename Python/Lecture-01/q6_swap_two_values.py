# Write a program to swap values of two numbers entered by the user.

num_1 = int(input("Enter a number : "))
num_2 = int(input("Enter another number : "))

num_1, num_2 = num_2, num_1

print(num_1, num_2)