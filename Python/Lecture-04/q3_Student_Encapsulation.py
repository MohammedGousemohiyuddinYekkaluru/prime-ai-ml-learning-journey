# Create a class Student with private attributes name, roll no, and marks. Provide getter and setter methods with validation (marks cannot be negative, roll number has to be between 1 - 100 and name cannot be empty)

class Student:

    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    def student_details(self):
        return f"Name: {self.__name}, Roll No: {self.__roll_no}, Marks: {self.__marks}"
    
    def set_name(self, name):
        if name.strip() == "":
            return "Name cannot be empty!"
        self.__name = name
        return "Name is updated"
    
    def set_roll_no(self, roll_no):
        if(roll_no <= 0 or roll_no >100):
            return "Roll number must be between 1 and 100!"
        self.__roll_no = roll_no
        return "Roll number is updated"
    
    def set_marks(self, marks):
        if(marks < 0):
            return "Marks cannot be negative"
        self.__marks = marks
        return "Marks updated"
    

student1 = Student("Gouse", 31, 75)

student1.set_name("Nizam")
student1.set_roll_no(22)
student1.set_marks(60)
print(student1.student_details())
