def calculate_grade(marks):
    if (marks>=70 and marks<=100):
     return 'A'

    elif (marks>=60 and marks<=69):
     return 'B'

    elif (marks>=50 and marks<=59):
     return 'C'

    elif (marks>=40 and marks<=49):
     return 'D'

    elif (marks>=0 and marks<40):
     return 'F'

    else:
     return 'Invalid'


#Input yor marks
marks = int(input("Enter your marks: "))

#Calling the function
grade = calculate_grade(marks)

#Printing the grade
print("Your grade is: ", grade)
