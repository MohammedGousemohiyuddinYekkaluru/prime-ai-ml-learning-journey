# Design a program to continuosly input a number from user and print if it is positive or negative until the user enters "Quit"


while True:
    user = input("Enter any Number or Quit")

    if(user == "Quit"):
        print("Over")
        break

    integer = int(user)

    if(integer > 0):
        print("Number is positive")
    elif(integer < 0):
        print("Number is negative")
    else:
        print("Number is Zero")