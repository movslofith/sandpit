def sum_num(xs):
    """ Sums all even or odd numbers in list xs depending on user preference
    """
    sum = 0
    odd_or_even = input("Enter 'odd' or 'even' to sum the respective number type from the list: ")
    
    if odd_or_even == "odd":
        for x in xs:
            if x % 2 != 0:
                sum = sum + x
        return sum

    if odd_or_even == "even":
        for x in xs:
            if x % 2 == 0:
                sum = sum + x
        return sum

    else:
        return "That is not a correct input of 'odd' or 'even'"

    
numbers = [1, 4, 6, 3, 2, 6, 7, 3, 7, 9, 14, -3, -5]

print(sum_num(numbers))


