def multiply_numbers(a: float, b: float) -> float:
    return a * b

def add_numbers(x: int, y: int) -> int:
    return x + y

def calculate_average(numbers: list) -> float:
    if len(numbers) > 0:
        return sum(numbers) / len(numbers)
    else:
        return 0.0
