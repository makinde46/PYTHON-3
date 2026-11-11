def convert_temperature(celcius):
    fahrenheit = (celcius*9/5)+32
    return fahrenheit

#Input the values
celcius = int(input("Enter temp in Celcius: "))

#Calling the function
temp = convert_temperature(celcius)

#Displaying the temp
print("The temp is: ", temp)
