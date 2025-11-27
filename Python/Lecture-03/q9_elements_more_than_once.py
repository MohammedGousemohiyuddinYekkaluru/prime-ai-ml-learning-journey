# Given a list, print all elements that appear more than once in the list

numbers = [1, 2, 3, 6, 2, 4, 1, 3]

numbers_dict = {}

for num in numbers:
    if num in numbers_dict:
        numbers_dict[num] += 1
    else:
        numbers_dict[num] = 1

print("Elements that appear more than once : ")

for num, count in numbers_dict.items():
    if count > 1:
        print(num)

