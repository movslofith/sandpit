def count_words_length_five(xs, y):
    """ Counts number of words in list 'xs' with length 'y' letters
    """
    counter = 0

    for x in xs:
        if len(x) == y:
            counter += 1

    return counter


words = ["cake", "beans", "chips", "gravy", "pizza", "pasta", "jam"]

print(count_words_length_five(words, 3))
