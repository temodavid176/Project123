import math

def calculate_surface_area(radius):
    """
    Calculate the surface area of a cylinder.
    
    Parameters:
    radius (float): The radius of the cylinder.
    
    Returns:
    float: The surface area of the cylinder.
    """
    pi = math.pi
    surface_area = 2 * pi * radius**2 + 2 * pi * radius * height
    return surface_area

def calculate_volume(radius, height):
    """
    Calculate the volume of a cylinder.
    
    Parameters:
    radius (float): The radius of the cylinder.
    height (float): The height of the cylinder.
    
    Returns:
    float: The volume of the cylinder.
    """
    pi = math.pi
    volume = pi * radius**2 * height
    return volume

def main():
    import sys
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <radius> <height>")
        exit(1)
    
    try:
        radius = float(sys.argv[1])
        height = float(sys.argv[2])
        
        surface_area = calculate_surface_area(radius)
        volume = calculate_volume(radius, height)
        
        print(f"Surface Area: {surface_area:.2f}")
        print(f"Volume: {volume:.2f}")
    
    except ValueError:
        print("Invalid input. Please provide numerical values for radius and height.")
        exit(1)

if __name__ == "__main__":
    main()
