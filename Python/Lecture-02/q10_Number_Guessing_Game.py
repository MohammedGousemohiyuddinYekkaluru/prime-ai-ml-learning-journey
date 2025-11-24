# Number Guessing Game

secret_num = 15

guess_num = int(input("Guess the Secret Number (from 1 to 20)"))

if(guess_num > secret_num):
    print("Too high")
elif(guess_num < secret_num):
    print("Too low")
else:
    print("Correct!")