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
    test(slope(5, 3, 4, 2) == 1)
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)
    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)


def slope(x1, y1, x2, y2):
    """ Returns slope of the line through points (x1, y1) and (x2, y2)
    """
    return (y2 - y1) / (x2 - x1)


def intercept(x1, y1, x2, y2):
    """ Returns y-intercept of line through points (x1, y1) and (x2, y2).
    """
    m = slope(x1, y1, x2, y2)
    c = y1 - (m * x1) 
    return c


test_suite()    # Here is the call to run the tests.