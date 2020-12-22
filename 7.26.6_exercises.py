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
    test(words_before_sam(["jim", "john", "sam", "steve"]) == 2)
    test(words_before_sam(["sam", "jim", "john"]) == 0)
    test(words_before_sam(["jim", "john", "clive"]) == 3)
    test(words_before_sam(["jim", "john", "clive", "samuel", "sam"]) == 4)


def words_before_sam(xs):
    """ Returns number of elements in a list before occurence of 'sam'.
    """
    count = 0 

    for x in xs:
        if x != "sam":
            count += 1
        else:
            break
    return count


test_suite()    # Here is the call to run the tests.
