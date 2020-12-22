def count_letters(word, letter):

    count = 0
    for character in word:
        if character == letter:
            count += 1
    return count

print(count_letters("banana", "a"))
