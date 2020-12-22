import sys

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILIED.".format(linenum))
    print(msg)


def sum_to(n):
    """ Return the sum of 1+2+3 ... n"""
    ss = 0
    v = 1
    while v <= n:
        ss = ss + v
        v = v + 1
    return ss

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(sum_to(4) == 10)
    test(sum_to(1000) == 500500)

test_suite()    # Here is the call to run the tests.