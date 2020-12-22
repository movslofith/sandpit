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
    test(num_digits(0) == 1)
    test(num_digits(-12345) == 5)


def num_digits(n):
    n = abs(n) # take the absolute value of n to avoid the infinite loop created by floor division of a negative number.
    count = 0
    if n == 0:
        count = 1

    while n != 0:
        count = count + 1
        n = n // 10
        
    return count

test_suite() # this is the call to run the unit tests

