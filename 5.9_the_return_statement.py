x = float(input("Give us a number to square root: "))

def print_square_root (x):
    if x <= 0:
        print("No zero or negative values please")
        return

    result = x ** 0.5
    print("The square root of", x, "is", result)

print_square_root(x)
