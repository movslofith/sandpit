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
    test(day_add("Monday", 4) == "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
   

def day_name(n):
    """ Converts integer number 0 to 6 into name of day
    """
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    if n in range(7):
        return days[n]
    else:
        return None 


def day_num(day):
    """ Converts name of day into integer number 0 to 6 
    """

    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    if day in days:
        return days.index(day)
    else:
        return None 


def day_add(current_day, delta_days):
    """ Given the current day (current_day - str), and the number of days in the future or past (delta_days - positive int), returns name of new day
    """
    return day_name((day_num(current_day) + delta_days) % 7 )
    

test_suite()    # Here is the call to run the tests.