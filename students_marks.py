#Creating The Marks
marks = [40,90,50,84,93]

#Printing Out The Marks
print(marks)
print(len(marks))
#Calculating The Total Marks And Displaying
total = sum(marks)
print("Total Marks is: ", total)

#Calculate and Display the Average Marks
average = total / len(marks)
print("Average Marks is: ", average)

#Display the Highest Marks
print("The Highest Marks is: ", max(marks))

#Display the Lowest Marks
print("The Lowest Marks is: ", min(marks))

#Modify the Third Subject
marks[2] = 65

#Display the Updated List
print("Updated marks is: ", marks)

