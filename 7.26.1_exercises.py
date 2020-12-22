def count_odd(xs):
    """ Counts number of odd numbers in list xs
    """
    counter = 0
    for x in xs:
        if x % 2 != 0:
            counter += 1

    return counter

numbers = [1, 4, 6, 3, 2, 6, 7, 3, 7, 9, 14, -3, -5]

print(count_odd(numbers))


