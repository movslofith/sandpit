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
    test(add_vectors([1, 1], [1, 1]) == [2, 2])
    test(add_vectors([1, 2], [1, 4]) == [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])

def add_vectors(u, v):
    """ Returns new list containing sum of corresponding elements of
    two input lists of same length. """
    new_vector = []
    for i in range(len(u)):
        #sum = u[i] + v[i]
        #new_vector.append(sum) 
        new_vector.append(u[i] + v[i])  # shorter way of doing it
    return new_vector


test_suite() # call to run the tests