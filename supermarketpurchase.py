#Calculate the total cost of the products purchased by the customer

customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
quantity = int(input("Enter quantity purchased: "))
price = float(input("Enter price per item: "))

total_cost = quantity * price

print(f"\nCustomer Name: {customer_name}")
print(f"Product Name: {product_name}")
print(f"Quantity: {quantity}")
print(f"Price: {price:.3f}")
print(f"Total Cost: {total_cost:.3f}")
