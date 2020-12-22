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
    test(remove("an", "banana") == "ba")
    test(remove("cyc", "bicycle") == "bile")
    test(remove("iss", "Mississippi") == "Mippi")
    test(remove("eggs", "bicycle") == "bicycle")


def remove(strg, word):
    """ Returns word with all instances of strg removed
    """
    strn_start_index = word.find(strg)

    if strn_start_index == -1:
        return word
        
    while strn_start_index != -1:
        strn_end_index = strn_start_index + len(strg)
        new_word = ""
        for x in range(0, strn_start_index):
            new_word += word[x]
        for x in range(strn_end_index, len(word)):
            new_word += word[x]
        word = new_word
        strn_start_index = word.find(strg)
    
    return new_word
    
    


test_suite() # call to run the tests