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
    ss = "Python strings have some interesting methods."
    test(find(ss, "s") == 7)
    test(find(ss, "s", 7) == 7)
    test(find(ss, "s", 8) == 13)
    test(find(ss, "s", 8, 13) == -1)
    test(find(ss, ".") == len(ss) - 1)
    
    test(ss.find("s") == 7)
    test(ss.find("ave", 3, 20) == 16)

def find(word, character, start=0, end=None):
    ix = start
    if end is None:
        end = len(word)
    while ix < end:
        if word[ix] == character:
            return ix
        ix += 1
    return -1 

test_suite() # call to runs the tests