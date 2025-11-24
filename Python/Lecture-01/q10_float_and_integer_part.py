# Take a float number as input and print the integer and fractinal part of that number

number = float(input("Enter a decimal number : "))

integer_part = int(number)
print(integer_part)

fractional_part = number - integer_part
print(fractional_part)