import math

x = int(input("What's the number? "))

if x < 0:
    print("THe negative number", x, "is not valid for the calculation we're about to do")
    x = 42
    print("We're going to use 42 instead")

print("The square root of", x, "is", math.sqrt(x))