# Create a student dictionary
student = {
    "registration_number": "REG001",
    "name": "John Kamau",
    "course": "Computer Science",
    "year_of_study": 1
}

# Display student's name and course
print("Student Name:", student["name"])
print("Course:", student["course"])

# Change the year of study
student["year_of_study"] = 2

# Add an email address
student["email"] = "john@gmail.com"

# Display the updated dictionary
print("\nUpdated Student Record:")
print(student)
