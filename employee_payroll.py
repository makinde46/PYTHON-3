class Employee:
    def __init__(self, employee_id, name, basic_salary, overtime_hours):
        self.employee_id = employee_id
        self.name = name
        self.basic_salary = basic_salary
        self.overtime_hours = overtime_hours

    def calculate_gross_salary(self):
        return self.basic_salary + (self.overtime_hours * 500)

    def calculate_tax(self):
        return self.calculate_gross_salary() * 0.10

    def calculate_net_salary(self):
        return self.calculate_gross_salary() - self.calculate_tax()


# Create two employee objects
employee1 = Employee("EMP101", "Alice", 50000, 10)
employee2 = Employee("EMP102", "Brian", 65000, 6)

# Display employee 1 details
print("Employee 1: Alice")
print("Gross Salary:", employee1.calculate_gross_salary())
print("Tax:", employee1.calculate_tax())
print("Net Salary:", employee1.calculate_net_salary())

print()

# Display employee 2 details
print("Employee 2: Brian")
print("Gross Salary:", employee2.calculate_gross_salary())
print("Tax:", employee2.calculate_tax())
print("Net Salary:", employee2.calculate_net_salary())