# Create an inventory dictionary
inventory = {
    "Sugar": 20,
    "Rice": 15,
    "Flour": 30,
    "Milk": 25,
    "Bread": 10
}

# Display the quantity of a specified product
print("Quantity of Rice:", inventory["Rice"])

# Add a new product
inventory["Cooking Oil"] = 12

# Update the quantity of an existing product
inventory["Sugar"] = 35

# Remove one product
del inventory["Bread"]

# Display the final inventory
print("\nFinal Inventory:")
print(inventory)