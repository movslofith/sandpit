import sys

def turn_clockwise(point):
    """ Takes compass point and returns compass point 90 degrees clockwise
    """
    compass_points = ["N", "E", "S", "W"]

    if point in compass_points:
        index = compass_points.index(point)
        new_index = (index + 1) % 4
        return compass_points[new_index]
    else:
        return None 

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
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)


test_suite()    # Here is the call to run the tests.