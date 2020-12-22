def is_rightangled(side_1, side_2, side_3):
    """
    Function to determine if triangle with sides of lengths side_1, side_2 and side_3 (with side_3 being the hypotenuse) is right-angled
    """
    hypo = (side_1 * side_1 + side_2 * side_2) ** 0.5
    if abs(hypo - side_3) < 0.000001:
        return True
    else:
        return False

sides = [] # create empty list for the sides of the triangle

# populate 'sides' list with 3 side length values from user

for i in range(3):
    print("What is the length of side length", i+1, "?")
    
    side_length = float(input())
    sides.append(side_length)


if is_rightangled(sides[0], sides[1], sides[2]) == True:
    print("It's right angled!")
else:
    print("That's not a right angled triangle.")