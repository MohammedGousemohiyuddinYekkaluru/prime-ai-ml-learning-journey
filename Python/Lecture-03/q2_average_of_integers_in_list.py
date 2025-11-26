#in a list of integers compute the average of all numbers in the list.

list_of_nums = [1, 2, 3, 4, 5]
sum = 0

for val in list_of_nums:
    sum += val

average = sum/len(list_of_nums)
print(average)