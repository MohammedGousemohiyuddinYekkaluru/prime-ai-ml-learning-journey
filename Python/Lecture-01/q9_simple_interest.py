# Ask the user for: principal, rate and time and calculate simple interest

principal = int(input("Enter principal : "))
rate = int(input("Enter rate : "))
time = int(input("Enter time : "))

simple_interest = (principal * rate * time)/100

print(simple_interest)