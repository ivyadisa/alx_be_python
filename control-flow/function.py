import math

def calculate_circle_area(radious):
    """Returns the area of the circle given the radious."""
    return math.pi * radious**2
    #example usage
r=float (input("Enter the radious of the circle : "))
area = calculate_circle_area(r)
print(f"The area of the circle with radious {r} is {area:.2f}")