# Create the classes: Herbivore, Carnivore, Omnivore with some attributes & methods. Then create a class Bear that inherits from all the above classes.


class Herbivore:
    def __init__(self, name):
        self.name = name
    
    def type(self):
        return f"{self.name} is a Herbivore"
    
class Carnivore:
    def __init__(self, name):
        self.name = name
    
    def type(self):
        return f"{self.name} is a Carnivore"

class Omnivore:
    def __init__(self, name):
        self.name = name
    
    def type(self):
        return f"{self.name} is a omnivore"
    
class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, name):
        super().__init__(name)

    def info(self):
        return f"{self.name} belongs to multiple categories."


b = Bear("Brown Bear")

print(b.type())  
print(b.info())


