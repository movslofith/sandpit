import string
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
    test(remove_punctuation('"Well, I never did!", said Alice.') == 'Well I never did said Alice')
    test(remove_punctuation("Are you very, very sure?") == "Are you very very sure")

def remove_punctuation(s):
    s_sans_punctuation = ""
    for letter in s:
        if letter not in string.punctuation:
            s_sans_punctuation += letter
    return s_sans_punctuation

test_suite() # call to run tests

my_story = """
Pythons are constrictors, which means that they will ’squeeze’ the life
out of their prey. They coil themselves around their prey and with
each breath the creature takes the snake will squeeze a little tighter
until they stop breathing completely. Once the heart stops the prey
is swallowed whole. The entire animal is digested in the snake’s
stomach except for fur or feathers. What do you think happens to the fur,
feathers, beaks, and eggshells? The ’extra stuff’ gets passed out as ---
you guessed it --- snake POOP! """

print(remove_punctuation(my_story).split())