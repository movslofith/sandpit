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
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    test(is_palindrome(""))


def reverse(s):
    reversed_word = ""
    for i in range(len(s), 0, -1):
        reversed_word += s[i-1]

    return reversed_word


def is_palindrome(word):
    """ Function recognises palindromes, returns true for palindrome, false otherwise
    """
    if word == reverse(word):
        return True
    return False
    

test_suite() # call to run the tests