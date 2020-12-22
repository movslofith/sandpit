import string


def count_letters(word, letter):
    """ Returns number of instances of 'letter' in 'word'
    """
    count = 0
    ix = 0
    while ix <= len(word):
        ind = word.find(letter, None, len(word))
        if ind != -1:
            count += 1
            word = word[ind + 1:]
        ix += 1
    
    return count

def find_letter(word, letter):
    """ Returns 1 if 'word' contains 'letter', returns 0 otherwise.
    """
    for i in word:
        if i == letter:
            return 1
    return 0

def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct


def text_analysis(text, letter):
    """ Removes all punctuation from 'text' string, counts the total words 
    and the number of words containing the 'letter' character.
    """
    count = 0 # variable for number of words containing 'letter'
    wds = remove_punctuation(text).split() # remove punctuation from text and split into list of words
    num_words = len(wds) # determine how many words in list 'wds'
    # find the number of words in 'wds' containing 'letter'
    for i in wds:
        if find_letter(i, letter) == 1:
            count += 1
    
    percent = (count / num_words) * 100 # determine the percentage of words containing 'letter'
    
    print("Your text contains", num_words, "words, of which", count, (percent,'%'), "contain an", "\"",letter,"\"")
        
    


para = """
If you can keep your head when all about you   
    Are losing theirs and blaming it on you,   
If you can trust yourself when all men doubt you,
    But make allowance for their doubting too;   
If you can wait and not be tired by waiting,
    Or being lied about, don’t deal in lies,
Or being hated, don’t give way to hating,
    And yet don’t look too good, nor talk too wise:

If you can dream—and not make dreams your master;   
    If you can think—and not make thoughts your aim;   
If you can meet with Triumph and Disaster
    And treat those two impostors just the same;   
If you can bear to hear the truth you’ve spoken
    Twisted by knaves to make a trap for fools,
Or watch the things you gave your life to, broken,
    And stoop and build ’em up with worn-out tools:

If you can make one heap of all your winnings
    And risk it on one turn of pitch-and-toss,
And lose, and start again at your beginnings
    And never breathe a word about your loss;
If you can force your heart and nerve and sinew
    To serve your turn long after they are gone,   
And so hold on when there is nothing in you
    Except the Will which says to them: ‘Hold on!’

If you can talk with crowds and keep your virtue,   
    Or walk with Kings—nor lose the common touch,
If neither foes nor loving friends can hurt you,
    If all men count with you, but none too much;
If you can fill the unforgiving minute
    With sixty seconds’ worth of distance run,   
Yours is the Earth and everything that’s in it,   
    And—which is more—you’ll be a Man, my son!
    """

text_analysis(para, "e")