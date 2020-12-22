def sum_even(xs):
    """ Sums all even numbers in list xs
    """
    sum = 0
    for x in xs:
        if x % 2 == 0:
            sum = sum + x

    return sum

numbers = [1, 4, 6, 3, 2, 6, 7, 3, 7, 9, 14, -3, -5]

print(sum_even(numbers))


