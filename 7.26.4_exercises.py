def count_words_length_five(xs):
    """ Counts number of words in list 'xs' with length 5 letters
    """
    counter = 0

    for x in xs:
        if len(x) == 5:
            counter += 1

    return counter


words = ["cake", "beans", "chips", "gravy", "pizza", "pasta", "jam"]

print(count_words_length_five(words))
