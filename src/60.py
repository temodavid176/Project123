def square_and_multiply(a: int, n: int) -> int:
    """
    Compute n^a mod p using Fermat's Little Theorem.
    
    Args:
        a (int): The base of the exponentiation.
        n (int): The exponent in the modulus operation.
        p (int): A prime number, must be coprime to n for correctness.
        
    Returns:
        int: The result of n^a mod p.
    """
    if p != 1 and n % p == 0:
        raise ValueError("n is not coprime with p")
    
    # Simplified version using Fermat's Little Theorem
    return pow(a, n, p)

# Example usage:
result = square_and_multiply(2, 3)
print(f"The result of 2^3 mod 5 is: {result}")
