# Create a base class Vehicle with attributes like brand and model. Create two subclasses Car and Bike that add extra attribues-seats and engine_cc

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

car1 = Car("Toyota", "carmy", 5)
bike1 = Bike("Yamaha", "R15", 155)

print(car1.brand, car1.model, car1.seats)
print(bike1.brand, bike1.model, bike1.engine_cc)