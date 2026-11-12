from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary

    def display_info(self):
        print("Name is :", self.__name)

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self,name,salary,employeeType):
        super().__init__(name,salary)
        self.employeeType = employeeType
        self.salary = salary

    def calculate_salary(self):
        return self.salary * 1.0
    
class PartTimeEmployee(Employee):
    def __init__(self,name,salary,employeeType):
        super().__init__(name,salary)
        self.employeeType = employeeType
        self.salary = salary

    def calculate_salary(self):
        return self.salary * 0.5

employee1 = FullTimeEmployee("Jeff",20000,"FullTime")
employee2 = PartTimeEmployee("John",30000,"PartTime")

employee1.display_info()
print("Salary is :", employee1.calculate_salary())

employee2.display_info()
print("Salary is :", employee2.calculate_salary())
        
