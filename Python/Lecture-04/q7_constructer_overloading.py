# Create a class Person that allows the constructer to work with name only, name + age, name + age + address. using default parameters

class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print("Name:", self.name)

        if self.age is not None:
            print("Age:", self.age)

        if self.address is not None:
            print("Address:", self.address)


p1 = Person("Rahul")
p2 = Person("Horrid", 22)
p3 = Person("Henry", 25, "Hyderabad")

p1.display()
p2.display()
p3.display()
