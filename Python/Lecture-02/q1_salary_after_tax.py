# Calculate salary after Tax

salary = int(input("Enter your salary : "))

if (salary < 30000):
    Tax = salary * 0.05
elif (salary > 30000 and salary < 70000):
    Tax = salary * 0.15
else:
    Tax = salary * 0.25

afterTax = salary - Tax

print("Salary After Tax:", afterTax)