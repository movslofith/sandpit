def find_hypot(side_1, side_2):
    """
    Function to return the length of hypotenuse of r-angle triangle given two short side lengths
    """
    hypo = (side_1 * side_1 + side_2 * side_2) ** 0.5
    return hypo

# a = float(input("What is the length of the first side? "))
# b = float(input("What is the length of the second side? "))
# print("The length of the hypotenuse is", find_hypot(a,b))

sides = [] # define list called 'sides' to contain the two short side lengths of the right angled triangle

for i in range(2):
    print("What is the length of side", i+1, "?")
    side_length = float(input())

    sides.append(side_length) # add inputted value to list

print("The length of the hypotenuse is", find_hypot(sides[0],sides[1]))
