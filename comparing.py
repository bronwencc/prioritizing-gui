# Code copyright 2021 by Github user bronwencc
#methods to compare lists and make logical inferences

#pick the non-empty above list to compare to the other's below list
def comparelists(list1, list2):
    '''
    Checks two lists of individual items for elements they have in common and
    returns the first item they share. If there are none in common or at least 
    one of the lists are empty, returns None.
    
    Params:
        list1 (list) : a list containing individual elements (no elements are 
                    themselves lists or dictionaries or array-likes; elements 
                    are Strings or numbers)
        list2 (list) : same properties as list1
    
    Returns:
        (list element) or None : the first of, if any, the items the two lists 
                                have in common; or null (None) if there are no 
                                items in common or both lists are empty
    '''
     #if one of the lists is empty, there is nothing to compare
    if list1==[] or list2==[]:
        return None #return null
    else:
        #find the intersection to see if they have any in common
        matches = list(set(list1) & set(list2))
        if matches == []: #if their intersection is an empty list
            return None #return null
        else: #return the first item in the intersected list
            return matches[0]
        
        
def infer(vals0,vals1):
    '''
    The method checks for whether an above list (first list in vals0 or vals1)
    has an item in common with a below list (second list in vals0 or vals1) of
    the other argument. If this is the case, it can be inferred that either the
    vals0 should rank higher than vals1 or the reverse is true.
    
    Params:
        vals0 (list) : three-element list of attributes related to an item in a
                        dataset. The first element is not important for this
                        function, the second element is a list of items from
                        the dataset that would be placed above the item related
                        to vals0, the third element is a list of items also
                        from the dataset that would rank below this item
                        associated with vals0.
        vals1 (list) : same qualities as vals0 but related to a different
                        item in the same dataset
    
    Returns:
        (boolean or None) : True (vals0 ranks higher), False (vals1 ranks
                            higher) or None (insufficient information)
    '''
    total0, above0, below0 = vals0
    total1, above1, below1 = vals1
    
    if [] == above0 == below0 == above1 == below1:#if all empty lists
        #there is no comparison to be made
        return None
    else:
        compared = comparelists(above1,below0)
        if compared != None:
            #vals1 above1 list shares an item with vals0 below0 list
            #compared ranks higher than vals1 and beneath vals0
            #so that would make vals0 item rank higher than vals1 item
            #since vals0 > compared > vals1
            return True #vals0 ranks higher than vals1
        else: #compare the other two above and below lists
            compared = comparelists(above0,below1)
            if compared != None: #vals0 above0 list shares an item with vals1 below1 list
#the item in compared is in above0 and below1, so it's a higher rank than vals0
#item, and a lower rank than vals1 item, so that would make the item related to
#vals1 rank higher than the item related to vals0 since vals1 > compared and
#compared > vals0
                return False #vals1 ranks higher than vals0

#compared was always None because there were no above-below list pairs that had
#any items in common
    return None #so no comparisons could be made