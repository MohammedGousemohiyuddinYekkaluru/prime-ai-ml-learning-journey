from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass


class Intern(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return f"Intern salary: {self.salary}"


class FullTimeEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return f"Full-time salary: {self.salary}"


class ContractEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return f"Contract salary: {self.salary}"



employees = [
    Intern(25000),
    FullTimeEmployee(60000),
    ContractEmployee(30000)
]

for employee in employees:
    print(employee.calculate_salary())

