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
    test(days_in_month("Febuary") == 28)
    test(days_in_month("December") == 31)
   

def days_in_month(month):
    """Takes name of month and returns number of days in that month
    """
    month_days = [31, 28, 31, 30, 31 ,30, 31, 31, 30, 31, 30, 31] # list of number of days in each month 
    months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"] # list of months
    if month in months:
        month_num = months.index(month)
        return month_days[month_num]
        # return month_days[months.index(month)]
    else:
        return None


test_suite()    # Here is the call to run the tests.