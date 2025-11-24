# Write a function that returns true if number is a prime number and false otherwise, using a loop


def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if(n % i == 0):
            return False
        else:
            return True

print(is_prime(5))