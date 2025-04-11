import math

def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

def area_of_circle(radius):
    return math.pi * radius ** 2

def sum_square_list(lst):
    return sum(x ** 2 for x in lst)

# Example usage
print(fibonacci(5))
print(is_prime(13))
print(area_of_circle(7.0))
print(sum_square_list([1, 4, 9]))
