class Employee:     
    def __init__(self,name,salary):         
        self.name=name         
        self.salary=salary 
class Manager(Employee):     
    def __init__(self,name,salary,department):         
        super().__init__(name,salary)        
        self.department=department     
    def display_info(self):         
        print("Name:",self.name)         
        print("Salary:",self.salary)         
        print("Department:",self.department) 
class Developer(Employee):     
    def __init__(self, name,salary,project):         
        super().__init__(name,salary)         
        self.project=project    
    def display_info(self):         
        print("Name:",self.name)         
        print("Salary:",self.salary)         
        print("Project:",self.project) 
manager=Manager("Ravi",80000,"HR") 
developer=Developer("laxmi",60000,"python project") 
manager.display_info() 
developer.display_info()