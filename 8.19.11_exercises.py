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
    test(count("is", "Mississippi") == 2)
    test(count("an", "banana") == 2)
    test(count("ana", "banana") == 2)
    test(count("nana", "banana") == 1)
    test(count("nanan", "banana") == 0)
    test(count("aaa", "aaaaaa") == 4)


def count(sub_stng, stng):
    """ Returns number of times substring occurs in string
    """
    instance_count = 0
    start_index = 0
    while stng.find(sub_stng, start_index) != -1:
        instance_count += 1
        start_index = stng.find(sub_stng, start_index) + 1

    return instance_count


test_suite() # call to run the tests