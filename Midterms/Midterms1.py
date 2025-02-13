def is_palindrome(number):
    return str(number) == str(number)[::-1]

def check_numbers(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    for index, line in enumerate(lines):
        numbers = list(map(int, line.strip().split(',')))
        total_sum = sum(numbers)
        if is_palindrome(total_sum):
            print(f"Line {index + 1}: {line.strip()} (sum {total_sum}) - Palindrome")
        else:
            print(f"Line {index + 1}: {line.strip()} (sum {total_sum}) - Not a palindrome")

# Example usage
check_numbers('numbers.txt')





