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
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")
   

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
    """ Given the current day (str), and the number of days in the future or past (int), returns name of new day
    """
    #a = day_num(current_day)   # find the number of the current_day
    #b = a + delta_days         # find the number of the new day
    #c = abs(b + 7) 
    #d = c % 7                  # reduce that day to a positive number <= 7
    #new_day_name = day_name(d) # find the name of that number day
    #return new_day_name
    
    return day_name(abs((day_num(current_day) + delta_days) % 7 )) # do the above steps all in one go
    
    

test_suite()    # Here is the call to run the tests.