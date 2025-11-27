# Create a dictionary with student names and marks and perform some operations depending on the user:


students = {
    "Rahul": 85,
    "Ayesha": 92,
    "Gouse": 88,
    "Amir": 76,
    "Priya": 95
}

while True:
    print("\n=== Choose the operation you want to do ===")
    print("A. Add a student")
    print("B. Update marks")
    print("C. Search for a student")
    print("D. Display all students and marks")
    print("E. Exit")

    choice = input("\nEnter Your Choice : ").upper()

    if(choice == "A"):
        student_name = input("\nEnter the name of the student : ")
        marks = int(input("Enter his marks : "))
        students[student_name] = marks

        print("\nStudent added succesfully")

    elif(choice == "B"):
         student_name = input("\nEnter the name of the student to update marks: ")

         if(student_name in students):
              new_marks = int(input(f"Enter new marks for {student_name}"))
              students[student_name] = new_marks
              print(f"\nMarks updated successfully for {student_name}.")
         else:
           print(f"\n{student_name} does not exist in the records.")

    elif(choice == "C"):
        student_name = input("\nEnter the name of the student : ")
        
        if(student_name in students):
            print(f"{student_name}'s marks are {students[student_name]}")
        else:
            print(f"{student_name} does not exist")

    elif(choice == "D"):
         print("\n--- Student Records ---")
         for name, marks in students.items():
            print(f"{name} : {marks}")

    elif(choice == "E"):
        print("Thank you!")
        break

    else:
        print("\n Invalid choice, Try again") 