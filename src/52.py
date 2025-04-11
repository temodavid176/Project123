import numpy as np

def calculate_area(shape):
    """
    Calculate the area of a shape.
    
    Args:
        shape (tuple): A tuple containing the dimensions of the shape. For example, (2, 4) for a square with side length 2.
        
    Returns:
        float: The area of the shape.
    """
    if not shape:
        raise ValueError("Shape must contain at least one dimension.")
    
    rows, cols = shape
    return rows * cols

print(calculate_area((3, 4)))
