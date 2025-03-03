firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = input("Enter your age: ")

fullName = firstName + " " + lastName
slice = firstName[:3]
message = f"Hello, {slice}! Welcome. You are {age} years old."

print("")
print("Full Name: " + fullName)
print("Sliced Name: " + slice)
print("Greeting Message: " + message)
