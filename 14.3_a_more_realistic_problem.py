import time

def load_words_from_file(filename):
    """ Returns list of words from filename
    """
    with open(filename) as f:
        file_content = f.read()
    my_substitutions = file_content.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_‘{|}~’'\\","abcdefghijklmnopqrstuvwxyz                                           ")
    cleaned_content = file_content.translate(my_substitutions)
    words = cleaned_content.split()
    return words

# print(load_words_from_file("vocab.txt"))
# print(load_words_from_file("alice_in_wonderland.txt"))

def find_unknown_words(words_file, vocab_file):
    """ Return a list of list of the words in words_file that do not occur in the vocab_file
    """
    result = []
    vocab = load_words_from_file(vocab_file)
    words_from_file = load_words_from_file(words_file)
    for w in words_from_file:
        if w not in vocab:
            result.append(w)
    return result

# print(find_unknown_words("alice_in_wonderland.txt", "vocab.txt"))

t0 = time.time()
missing_words = find_unknown_words("alice_in_wonderland.txt", "vocab.txt")
t1 = time.time()
print("There are {0} missing words".format(len(missing_words)))
print("That took {0:.4f} seconds".format(t1-t0))

