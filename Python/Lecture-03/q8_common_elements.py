# Write a program to check whether two lists share no common elements...

list1 = [1,2,3,4,5]
list2 = [5,6,7,8]

if set(list1).intersection(set(list2)): # we can use .isdisjojnt() also
    print("The lists have common elements")
else:
    print("The lists have no common elements")
