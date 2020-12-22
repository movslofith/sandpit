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
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))
    
    
def is_prime(n):
    """ Returns True when single integer argument is a prime number and False otherwise.
    """
    divisor = n - 1
    while divisor > 1:
        if n % divisor == 0:
            return False
        else:
            divisor -= 1
            continue
    return True

test_suite() # this is the call to run the tests in test_suite