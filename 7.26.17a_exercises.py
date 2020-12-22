def play_once(human_plays_first):
    """ Must play one round of the game, if the parameter
    is True, the human gets to play first, else the 
    computer gets to play first. When the round ends,
    the return value of the function is one of
    -1 (human wins), 0 (game drawn), 1 (computer wins).
    """
    # dummy scaffolding code
    import random
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1, 2)
    print("Human plays first={0}, winner={1} ".format(human_plays_first, result))

    return result

human_plays_first = 0

while True:
    result = play_once(human_plays_first)
    if result == 1:
        print("I win!")
    elif result == 0:
        print("Game drawn!")
    else:
        print("You win!")

    response = input("Would you like to play again? (Y or N)")
    if response == "N":
        break

print("Goodbye!")

