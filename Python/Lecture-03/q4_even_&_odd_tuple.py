#From a tuple of integers, create a tuple of all even & odd numbers

numbers = (1, 2, 3, 4, 5, 6)

even = ()
odd = ()

for val in numbers:
    if(val % 2 == 0):
        even += (val,)
    else:
        odd += (val,)   

print(odd)
print(even)
