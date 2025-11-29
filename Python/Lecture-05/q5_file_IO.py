# Write a program that tries to open a file in read mode. if the file does not exist, catch the exception and print "File not found!".

try:
    with open("data.txt", "r") as f:
        data = f.read()
        print(data)

except FileNotFoundError:
    print("File not found!")

finally:
    print("Program finished Successfully!")
    