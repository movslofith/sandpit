def load_words_from_file(filename):
    """ Returns list of words from filename
    """
    with open(filename) as f:
        file_content = f.read()
    my_substitutions = file_content.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_‘{|}~’'\\","abcdefghijklmnopqrstuvwxyz                                           ")
    cleaned_content = file_content.translate(my_substitutions)
    words = cleaned_content.split()
    return words

def remove_adjacent_duplicates(xs):
    """ Return a new list in which all duplicates in xs are removed
    """
    result = []
    most_recent_element = None
    xs.sort()
    for e in xs:
        if e != most_recent_element:
            result.append(e)
            most_recent_element = e
    
    return result

def search_binary(xs, target):
    """ Return index of target in sequence xs
    """
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub: # if region of interest (ROI) becoming empty
            return -1
        
        mid_index = (lb + ub) // 2

        item_at_mid = xs[mid_index]

        print("ROI[{0}:{1}](size = {2}, probed=' {3}', target=' {4}'".format(lb, ub, ub-lb, item_at_mid, target))

        if item_at_mid == target:
            return mid_index
        if item_at_mid < target:
            lb = mid_index + 1
        else:
            ub = mid_index
            

vocab = load_words_from_file("alice_in_wonderland.txt")

vocab = remove_adjacent_duplicates(vocab)
print(vocab)

search_binary(vocab, "magic")
