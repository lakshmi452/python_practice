from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary
    def calculate_salary(self):
        print("Full Time Salary:", self.salary)
class PartTimeEmployee(Employee):
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate
    def calculate_salary(self):
        salary = self.hours * self.rate
        print("Part Time Salary:", salary)
e1 = FullTimeEmployee(40000)
e2 = PartTimeEmployee(25, 600)
e1.calculate_salary()
e2.calculate_salary()