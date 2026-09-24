def calculate_bill(units):
    if (unit_consumption>0 and unit_consumption<=100):
        return 15
    elif (unit_consumption>100 and unit_consumption<=300):
        return 20
    elif (unit_consumption>300):
        return 25
units = int(input("Enter no. of units consumed: "))
charges = calculate_bill(units)
bill = charges + 100

print(f"The number of units consumed ={units}, charges = {charges}")
print(f"The total bill", bill)
