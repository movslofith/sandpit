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
    test(is_even(2) == True)
    test(is_even(0) == True)
    test(is_even(-8) == True)
    test(is_even(5.4) == False)
    test(is_even(3) == False)
    test(is_odd(1) == True)
    test(is_odd(-3) == True)
    test(is_odd(0) == False)
    test(is_odd(4) == False)

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return not is_even(n)

test_suite()    # Here is the call to run the tests.