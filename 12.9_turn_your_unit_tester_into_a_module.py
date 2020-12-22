# having put the unit testing function into a module of its own
# now to test using it, with 11.22.7_exercises as an example

from unit_tester import test

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(dot_product([1, 1], [1, 1]) == 2)
    test(dot_product([1, 2], [1, 4]) == 9)
    test(dot_product([1, 2, 1], [1, 4, 3]) == 12) 


def dot_product(u, v):
    """ Returns sum of products of corresponding elements of u and v """
    total = 0
    for i in range(len(u)):
        total = total + (u[i] * v[i])
    return total


test_suite() # call to run the tests