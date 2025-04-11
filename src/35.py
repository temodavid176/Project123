import math

def calculate_square_root(number):
    if number < 0:
        raise ValueError("Square root of negative numbers is not defined.")
    return math.sqrt(number)

try:
    print(calculate_square_root(16))
except ValueError as e:
    print(e)
