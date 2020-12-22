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
    test(find("Compsci", "p") == 3)
    test(find("Compsci", "C") == 0)
    test(find("Compsci", "i") == 6)
    test(find("Compsci", "x") == -1)

def find(word, character):
    """
    Find and return the index of a character (case sensitive and first instance of) in string.
    Return -1 if character does not occur in string
    """
    ix = 0
    while ix < len(word):
        if word[ix] == character:
            return ix
        ix += 1
    return -1

test_suite() # call to runs the tests