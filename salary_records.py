# Create an employees dictionary
employees = {
    "John": 30000,
    "Mary": 35000,
    "Peter": 40000,
    "Jane": 32000,
    "David": 45000
}

# Display all employee names and salaries using a loop
print("Employee Salary Records:")
for name, salary in employees.items():
    print(name, ":", salary)

# Update the salary of one employee
employees["John"] = 38000

# Add a new employee and salary
employees["Grace"] = 42000

# Calculate the total salary payable
total_salary = sum(employees.values())

# Display the total salary
print("\nTotal Salary Payable:", total_salary)