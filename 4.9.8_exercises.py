import math

def area_of_circle(r):
    """
    Calculates area of circle radius r.
    Returns area.
    """
    area = math.pi * r ** 2


    return area

# one way of getting the input and printing the answer

r = float(input("What is the radius of your circle? "))

print("The area of your circle of radius", r, "is", area_of_circle(r))

# another way of achieving the same 

print("The area of your circle is", area_of_circle(float(input("What is the radius of your circle? "))))
