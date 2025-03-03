firstName = input("Enter first name: ")
lastName = input("Enter last name: ")
age = input("Enter age: ")
contactNumber = input("Enter contact number: ")
course = input("Enter course: ")
personalInfo = f"{lastName}, {firstName}, {age}, {contactNumber}, {course}\n"

with open("students.txt", "a") as file:
    file.write(personalInfo)

print("Student information has been saved to 'students.txt'.")
