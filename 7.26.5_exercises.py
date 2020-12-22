import sys

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILIED.".format(linenum))
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(sum_before_first_even([1, 3, 5, 7, 8]) == 16)
    test(sum_before_first_even([0, 0, 1]) == 0)
    test(sum_before_first_even([2, 5, 2]) == 0)
    test(sum_before_first_even([-1, -5, 3, 6]) == -3)
    test(sum_before_first_even([2, 4, 6, 8]) == 0)
    test(sum_before_first_even([1, 3, 5, 7]) == 16)


def sum_before_first_even(xs):
    """ Returns sum of all elements in a list up to but not including the first even number
    """
    sum = 0 

    for x in xs:
        if x % 2 != 0:
            sum = sum + x
        else:
            break
    return sum


test_suite()    # Here is the call to run the tests.
