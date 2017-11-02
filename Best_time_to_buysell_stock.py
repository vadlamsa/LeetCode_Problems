"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find
the maximum profit.
Example 1:

Input: [7, 1, 5, 3, 6, 4]
Output: 5
max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

"""
def stock(lst):
    maxe = 0  # max element i.e the selling price
    mine = lst[0]  # min elem i.e the buying price
    result = None
    minindex = None
    maxindex = lst.index(max(lst))
    l = len(lst)
    for elem in lst:
        #  mine  cannot be the last element because then there will be no selling price.
        if elem < mine and lst.index(elem) != l-1:
           mine = elem
    minindex = lst.index(mine)
    if maxindex > minindex:
        pass
    else:
        for elem in lst:
        # maxe has to come after mine indicating that selling price > buying price
            if elem > maxe and lst.index(elem) > minindex:
               maxe = elem
        if maxe > mine:
            maxindex = lst.index(maxe)
            print 'largest number is',maxe
            print 'profit is',maxe - mine
            result = maxe - mine
        else:
            print("Cannot perform transaction")
            result = None
        return result
if __name__ == '__main__':
    assert (stock([7, 1, 5, 3, 6, 4])) == 5
    assert (stock([1,2,3,4])) == None
