#Expense Tracker Project

expenses = [] #list of all expenses in form of dictionaries

print("Welcome to Expense Tracker")

while True:
    print("\n ==== MENU ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total amount")
    print("4. Exit")

    choice = int(input("\n Please Enter Your Choice : "))

    if(choice == 1):
        date = input("Enter the date : ")
        category = input("Enter the category (Food, Cloth, Travel, Stationary, etc.,) : ")
        description = input("Enter some details of the category: ")
        amount = float(input("Enter the amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("\n Expense added Succesfully")
    elif(choice == 2):
        if(len(expenses) == 0):
            print("No expense are added")
        else:
            print("===== These are your Expenses =====")
            count = 1
            for eachExpense in expenses:
                print(f"Expense No.{count} -> {eachExpense["date"]}, {eachExpense["category"]}, {eachExpense["description"]}, {eachExpense["amount"]}")
            count += 1

    elif(choice == 3):
        total = 0
        for eachAmount in expenses:
            total += eachAmount["amount"]
        
        print(f"\n Your total amount is {total}")

    elif(choice == 4):
        print("\n Thank you for using this Expense tracker")
        break
    else:
        print("\n Invalid choice, Try again") 
