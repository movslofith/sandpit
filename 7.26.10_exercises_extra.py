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
    

def sqrt(n):
    approx = n/2.0
    while True:
        better = (approx + n/approx)/2.0
        if abs(approx - better) < 0.000001:
            return better
        approx = better 


def is_prime(n):
    """ Returns True when single integer argument is a prime number and False otherwise.
    """
    for i in range(2, int(sqrt(n)) + 1): # using primality test of whether integer between 2 and sqrt(n) divides n evenly (leaving no remainder)
        if n % i == 0:
            return False
        else:
            continue
    return True

test_suite() # this is the call to run the tests