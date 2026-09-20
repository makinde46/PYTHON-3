"""
This program stores and displays basic employee information.
It demonstrates variables, Boolean values, f-string formatting,
and converting a number to a string using str().
"""

#Create variables and assign suitable values
employee_name = "John Kamau"
employee_age = 28
employee_salary = 75000
employee_active_status = True

#Display all employee information using f-string formatting
print(f"Employee Name: {employee_name}")
print(f"Employee Age: {employee_age}")
print(f"Employee Salary: Ksh {employee_salary}")
print(f"Employee Active Status: {employee_active_status}")

#Convert a number to a string before concatenating
age_string = str(employee_age)
print("Employee age is " + age_string + " years old.")
