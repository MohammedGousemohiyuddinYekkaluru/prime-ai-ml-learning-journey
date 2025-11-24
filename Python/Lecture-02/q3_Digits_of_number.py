# Writea function that prints the digits of a number

def get_digits(num):
    digits = []
    while num > 0:
        digits.append(num % 10) # This gets last digit of the number and appends it to the digits list
        num //= 10 # This removes the last digit from the number

    for d in reversed(digits):
        print(d)

get_digits(234)