class Employee:
    def __init__(self,name,ID,age,email):
        self._name = name
        self.__ID = ID
        self.age = age
        self.email = email

    def display(self):
        print("Name :", self._name)
        print("ID :", self.__ID)
        print("Age :", self.age)
        print("Email :",self.email)

class SalariedEmployee(Employee):
    def __init__(self,name,ID,age,email,salary):
        super().__init__(name,ID,age,email)
        self.salary = salary

    def __display(self):
        super().display()
        print("Salary : ", self.salary)

try:
    emp = SalariedEmployee("Jeff",12345,21,"jeff@gmail.com",30000)
    emp._display()
except Exception as e:
    print(f"An error has occured")
else:
    print("Code runs")
finally:
    print("Code runs anyways")
