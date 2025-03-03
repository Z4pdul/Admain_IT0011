with open("students.txt", "r") as file:
    studentInfo = file.readlines()

print("Reading Student Information:")
for line in studentInfo:
    lastName, firstName, age, contactNumber, course = line.strip().split(", ")
    
    print(f"\nLast Name: {lastName}")
    print(f"First Name: {firstName}")
    print(f"Age: {age}")
    print(f"Contact Number: {contactNumber}")
    print(f"Course: {course}")
    
    #Question and Answer
    
    #1. How does the format() function help in combining variables with text in Python? Can you provide a simple example?
    #The format() function in Python helps us combine the variables with the text easily. By using the {} we can use the format() function to replace  them with the values of the variables
    #integer = 5
    #message = "The given integer is {}".format(integer)
    #print(integer)
    
    #2. Explain the basic difference between opening a file in 'read' mode ('r') and 'write' mode ('w') in Python. When would you use each
    #The read mode is used to open a file for reading. you can only look at the content, and the file itself must be already existing.
    #you will only use it when you just want to read the content of the file.
    #The Write mode is used to open a file for writing. You will be able to write the contents in a file, if the file is not existing, then it will create a new file
    #you use it when you want to create a new file or just change the current content of the files.
    
    #3. Describe what string slicing is in Python. Provide a basic example of extracting a substring from a larger string.
    #String slicing is when you take part of a string called a substring, from a larger string.
    #message = "Hello, Abdul!"
    #substring = message[7:12]
    #print(substring)
    #output = Abdul
    
    #4. When saving information to a file in Python, what is the purpose of using the 'a' mode instead of the 'w' mode? Provide a straightforward example.
    #The purpose of the 'a' mode is to add new information to the end of an already existing file without removing ehat is already there.
    #while the 'w' mode, will erase the existing content of the file before writing a new one.
    #with open('students.txt', 'w') as file:
    #file.write('Abdullah Admain\n') this erases any previous content
    #with open('students.txt', 'a') as file:
    #file.write('Abdullah Admain\n') adds "Abdullah Admain" to the end of the existing content, but still keeping the previous text
    
    #5.Write a simple Python code snippet to open and read a file named "data.txt." How would you handle the case where the file might not exist?
    #I will use try and except to handle errors
    #try:
    #   with open('data.txt', 'r') as file:
    #       content = file.read()
    #       print(content)
    #except FileNotFoundError:
    #   print("The file does not exist.")