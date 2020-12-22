import random

def make_random_ints(num, lower_bound, upper_bound):
    """
    Generate a list containing num random integers between lower_bound
    and upper_bound. Upper bound is an open bound.
    """
    rng = random.Random() # create a random number generator
    result = []
    for i in range(num):
        result.append(rng.randrange(lower_bound, upper_bound))
    return result

print(make_random_ints(100, 3, 11))

# what if you want 5 numbers between 1 and 12 with no duplicates?

xs = list(range(1, 13)) # create a list 1 ... 12
rng = random.Random() # make a random number generator
rng.shuffle(xs) # shuffle the list
print(xs[:5]) # take the first five elements

# this above method works when the range of possible numbers is small
# for a large range the above method of generating a list of all 
# possible values first would be very inefficient


def make_random_ints_no_dups(num, lower_bound, upper_bound):
    """
    Generate a list containing num random integers between lower_bound
    and upper_bound. upper_bound is an open bound. The result list cannot
    contain duplicates.
    """
    result = []
    rng = random.Random()
    for i in range(num):
        while True:
            candidate = rng.randrange(lower_bound, upper_bound)
            if candidate not in result:
                break
        result.append(candidate)

    return result


x = make_random_ints_no_dups(10, 2, 40)
print(x)



