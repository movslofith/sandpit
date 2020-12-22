import math

def f(r):
    """ Return (circumference, area) of a circle of radius r) """
    c = 2 * math.pi * r
    a = math.pi * r**2
    return (c, a)

print("The area of circle radius 5 is:", f(5)[1])