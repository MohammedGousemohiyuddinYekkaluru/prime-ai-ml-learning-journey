# Write a function to return the count of the number of digits in a number

def getNumberOfDigits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

number_of_digits = getNumberOfDigits(543)
print(number_of_digits)