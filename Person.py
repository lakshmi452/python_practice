class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,attendance):
        super().__init__(name,age)
        self.attendance=attendance
    def display_info(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Attendance:",self.attendance)
class Teacher(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    def display_info(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Salary:",self.salary)
student=Student("Suchi",20,90)
teacher=Teacher("Madhavi",40,90000)
student.display_info()
teacher.display_info()