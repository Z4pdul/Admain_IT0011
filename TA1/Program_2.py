string = input("Enter a string containing digits: ")
sum = 0

for char in string:
    if char.isdigit():
        sum += int(char)

print("The sum of digits is", sum)