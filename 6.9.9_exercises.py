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
    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)

def hours_in(total_seconds):
    return int(total_seconds / 3600)

def minutes_in(total_seconds):
    return int((total_seconds - hours_in(total_seconds) * 3600) / 60)
    #a = total_seconds % 3600 # just another way of doing it (easier to debug)
    #return a
def seconds_in(total_seconds):
    return total_seconds - (hours_in(total_seconds) * 3600) - (minutes_in(total_seconds) * 60)
    #a = total_seconds % 3600 # easier to debug this way
    #b = a % 60
    #return b


test_suite()    # Here is the call to run the tests.