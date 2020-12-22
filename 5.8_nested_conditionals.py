x = int(input("What number is it? "))

if 0 < x:
    if x < 10:
        print("x is a single positive digit")

if 0 < x and x < 10:
    print("x is a single positive digit")

else:
    print("x is either negative or not a single positive digit")

