def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx * dx + dy * dy
    result = dsquared ** 0.5
    return result

def area(radius):
    b = 3.14159 * radius ** 2
    return b

def area2(xc, yc, xp, yp):
    """
    Function to return the area of a circle defined by centre point (xc, yc) and a point on the perimeter (xp, yp).
    """
    # radius = distance(xc, yc, xp, yp)
    # result = area(radius)
    # return result
    
    return area(distance(xc, yc, xp, yp))

area2(2, 2, 9, 11)