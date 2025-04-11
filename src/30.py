def add_numbers(a, b):
    result = a + b
    return result

def subtract_numbers(a, b):
    result = a - b
    return result

def multiply_numbers(a, b):
    result = a * b
    return result

def divide_numbers(a, b):
    if b != 0:
        result = a / b
        return result
    else:
        return "Error: Division by zero is not allowed."

def calculate_and_display(expression):
    try:
        expression = str(expression).split()  # Convert the string to a list of elements
        first_number, operator, second_number = expression[0], expression[1], expression[2]
        
        if operator == '+':
            result = add_numbers(int(first_number), int(second_number))
            print(f"The sum is {result}")
        elif operator == '-':
            result = subtract_numbers(int(first_number), int(second_number))
            print(f"The difference is {result}")
        elif operator == '*':
            result = multiply_numbers(int(first_number), int(second_number))
            print(f"The product is {result}")
        elif operator == '/':
            if second_number != 0:
                result = divide_numbers(int(first_number), int(second_number))
                print(f"The quotient is {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Error: Invalid operator. Please use +, -, *, or /.")

if __name__ == "__main__":
    user_input = input("Enter an expression (e.g., '3 + 5 * 2'): ")
    calculate_and_display(user_input)
