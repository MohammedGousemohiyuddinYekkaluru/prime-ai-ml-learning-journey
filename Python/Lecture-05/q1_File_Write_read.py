# Create a program that: 1) Opens a file "names.txt" in write mode. 2) Writes 5 names(one per line) entered by the user. 3) Then opens the same file in read mode and prints all names...

with open("names.txt", "w") as f:

    for i in range(5):
        name = input(f"Enter name {i + 1}: ")
        f.write(name + "\n")

with open("names.txt", "r") as f:
    names = f.read()
    print(names)