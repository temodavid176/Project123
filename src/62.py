import math

def area_of_triangle(base, height):
    """
    Calculate the area of a triangle using base and height.
    
    Args:
    base (float): The length of the base of the triangle.
    height (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    """
    return 0.5 * base * height

def main():
    print("Triangle area calculation example:")
    base = float(input("Enter the base length: "))
    height = float(input("Enter the height: "))
    area = area_of_triangle(base, height)
    print(f"The area of the triangle with base {base} and height {height} is: {area:.2f}")

if __name__ == "__main__":
    main()
