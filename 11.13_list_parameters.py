def double_stuff(a_list):
    """ overwrite each element in a list with double it's value"""
    for (idx, val) in enumerate(a_list):
        a_list[idx] = 2 * val

things = [2, 5, 7]
double_stuff(things)
print(things)