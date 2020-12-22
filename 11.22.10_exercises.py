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
    test(replace("Mississippi", "i", "I") == "MIssIssIppI")

    s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
    test(replace(s, "om", "am") == "I love spam! Spam is my favorite food. Spam, spam, yum!")

    test(replace(s, "o", "a") == "I lave spam! Spam is my favarite faad. Spam, spam, yum!")


def replace(s, old, new):
    words = s.split(old)
    new_words = new.join(words)
    
    return new_words

test_suite() # call to run the tests