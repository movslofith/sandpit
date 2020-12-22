def print_multiples(n, x):
    """Prints line of multiples of n up to final multiple x, then starts new line.
    """ 
    for i in range(1, x):
        print(n * i, end="\t")
    print()


def print_mult_table(x, y):
    """Prints multiplication table of size x, y starting from zero with increments of 1.
    """
    for i in range (1, y + 1):
        print_multiples(i, x + 1)


print_mult_table(10, 10)

