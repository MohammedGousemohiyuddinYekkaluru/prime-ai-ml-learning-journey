# Write a function that takes two integers and prints all even numbers between them (inclusive)

def getEvenNumbers(a, b):
    for i in range(a, b + 1):
        if( i % 2 == 0):
            print(i)

getEvenNumbers(1, 10)


