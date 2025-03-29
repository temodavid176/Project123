def sum_of_odd_numbers(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            total += i
    return total

# Example usage
print(sum_of_odd_numbers(10))  # Output: 25 (3 + 5 + 7 + 9)
