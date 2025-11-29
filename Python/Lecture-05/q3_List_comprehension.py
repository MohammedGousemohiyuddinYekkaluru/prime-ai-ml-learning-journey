# Create a program using a list comprehension to create a new list with only numbers greater than 15, print the new list

numbers = [5, 10, 15, 20, 25, 30]

nums = [x for x in numbers if x > 15]

print(nums)