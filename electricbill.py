def calculate_bill(units_consumed,cost_per_unit):
    bill = units_consumed*cost_per_unit
    return bill

#User input values
units = int(input(f"Enter units consumed: "))
cost = int(input(f"Enter cost per unit: "))

#Calling the function
bill = calculate_bill(units, cost)

#Display the bill
print("Yor electricity bill is: ", bill)
