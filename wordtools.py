from unit_tester import test

def cleanword(s):
    """ Returns string s with any punctuation removed
    """
    import string
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter

    return s_without_punct

def has_dashdash(s):
    """ Returns True if string s contains two dashes immediately after one another
    """ 
    return "--" in s

def extract_words(s):
    """Removes punctuation and capitalisation from string and returns individual words
    """
    new_list = [] # list container for list of words
    if has_dashdash:
        s = " ".join(s.split("--"))
    s = cleanword(s) # remove all punctuation from string
    s = s.lower() # make string all lower case
    new_list = s.split(" ") # separate individual words of string
    return new_list

def wordcount(word, word_list):
    """ Returns count of the number of times word appears in word_list
    """
    counter = 0
    for i in word_list:
        if i == word:
            counter += 1
    return counter

def wordset(word_list):
    """ Returns word_list with duplications of instances removed sorted into alphabetical order
    """
    new_list = []
    for i in word_list:
        if i not in new_list:
            new_list.append(i)
            new_list = sorted(new_list)
    return new_list

def longestword(word_list):
    """ Returns length (int) of the longest word in word_list
    """
    if word_list:
        word_length = len(max(word_list, key=len))
    else:
        word_length = 0
    return word_length

test(cleanword("what?") == "what")
test(cleanword("'now!'") == "now")
test(cleanword("?+-'w-o-r-d!,@$()'") == "word")

test(has_dashdash("distance--but"))
test(not has_dashdash("several"))
test(has_dashdash("spoke--"))
test(has_dashdash("distance--but"))
test(not has_dashdash("-yo-yo-yo-"))

test(extract_words("Now is the time! 'Now', is the time? Yes, now.") 
== ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now'])
test(extract_words("she tried to curtsey as she spoke--fancy") 
== ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy'])

test(wordcount("now", ["now", "is", "time", "is", "now", "is", "is"]) == 2)
test(wordcount("is", ["now", "is", "time", "is", "now", "the", "is"]) == 3)
test(wordcount("time", ["now", "is", "time", "is", "now", "is", "is"]) == 1)
test(wordcount("frog", ["now", "is", "time", "is", "now", "is", "is"]) == 0)

test(wordset(["now", "is", "time", "is", "now", "is", "is"]) == 
["is", "now", "time"])
test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) == 
["I", "a", "am", "is"])
test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
["a", "am", "are", "be", "but", "is", "or"])

test(longestword(["a", "apple", "pear", "grape"]) == 5)
test(longestword(["a", "am", "I", "be"]) == 2)
test(longestword(["this", "supercalifragilisticexpialidocious"]) == 34)
test(longestword([ ]) == 0)
