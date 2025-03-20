def divide(a, b):
    if b == 0:
        print("Error! The denominator must not be equal to zero.")
        return None
    return a / b

def exponentiate(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        print("Error! The denominator must not be equal to zero.")
        return None
    return a % b

def summation(start, end):
    if end <= start:
        print("Error: The second number must be greater than the first number.")
        return None
    return sum(range(start, end + 1))

def main():
    while True:
        print("\nMenu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")

        choice = input("Enter your choice: ").strip().upper()

        if choice == "Q":
            print("Exiting program. Goodbye!")
            break
        elif choice in ["D", "E", "R", "F"]:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                
                if choice == "D":
                    result = divide(num1, num2)
                elif choice == "E":
                    result = exponentiate(num1, num2)
                elif choice == "R":
                    result = remainder(num1, num2)
                elif choice == "F":
                    result = summation(int(num1), int(num2))
                
                if result is not None:
                    print(f"Result: {result}")
            except ValueError:
                print("Error! Please enter a valid number.")
        else:
            print("Invalid choice. Please try agains.")

if __name__ == "__main__":
    main()