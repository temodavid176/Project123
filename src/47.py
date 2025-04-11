import numpy as np

def add_vectors(v1, v2):
    """
    Add two vectors represented by lists or numpy arrays.
    
    Args:
        v1 (list or numpy.ndarray): The first vector.
        v2 (list or numpy.ndarray): The second vector.
        
    Returns:
        list or numpy.ndarray: The resulting vector after addition.
    """
    return [a + b for a, b in zip(v1, v2)]

# Example usage
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

result_vector = add_vectors(vector1, vector2)
print(result_vector)  # Output: [5, 7, 9]
