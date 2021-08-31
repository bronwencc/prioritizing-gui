#using itertools to create pairs by default
from itertools import combinations

def combos(itemlist, n=2):
    '''
    This function takes in a list or arraylike and uses combinations from
    itertools to return combinations of the items in a list. The order of the
    items in the combinations is not taken into account.

    Params:
        n (int > 0) : the size of the combination; how many to draw from itemlist 
                    at a time, defaults to 2
        itemlist (arraylike) : a list of items to be combined into groups
                               of n size, preferably each item is a String or 
                               individual (not one element containing a list)
    Returns:
        (list) : combinations of tuples of size n, containing all variations
                (without regard to order) of elements from itemlist
    '''
    return list(combinations(itemlist, n))