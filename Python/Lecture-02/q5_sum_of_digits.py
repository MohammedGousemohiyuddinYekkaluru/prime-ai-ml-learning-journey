# Write a function to return the sum of digits of a number

def getSumOfDigits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

sum_of_digits = getSumOfDigits(12345)
print(sum_of_digits)