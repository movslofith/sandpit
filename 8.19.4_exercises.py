def count_letters(word, letter):
    count = 0
    ix = 0
    while ix <= len(word):
        ind = word.find(letter, None, len(word))
        if ind != -1:
            count += 1
            word = word[ind + 1:]
        ix += 1
    
    return count

print(count_letters("banana", "a"))
