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
    test(remove_vowels("compsci") == "cmpsc")
    test(remove_vowels("aAbEefIijOopUus") == "bfjps")


def remove_vowels(s):
    """ Returns string input with vowels removed
    """
    vowels = "aAeEiIoOuU"
    s_sans_vowels = ""
    for x in s:
        if x not in vowels:
            s_sans_vowels += x
    return s_sans_vowels

test_suite() # call to runs the tests