from unit_tester import test

def myreplace(old, new, s):
    """ Replace all occurences of old with new in s."""
    return new.join(s.split(old))

test(myreplace(",", ";", "this, that, and some other thing") == "this; that; and some other thing")
test(myreplace(" ", "**", "words will now be separated by stars.") == "words**will**now**be**separated**by**stars.")

