# coding=utf-8
"""
Given an array with both positive and negative numbers. We need to find the two elements such
that their sum is closest to zero. For the below array, algorithm should give −80 and 85.
Example:
		[1,60,− 10,70,− 80,85]
"""
# Method 1: Brute force. O(n2) time complexity
'''
def f(lst):
    minsum = lst[0] + lst [1]
    min_i = 0
    min_j = 1
    for i in range(len(lst)):
        for j in range(1,len(lst)):
            sm = lst[i] + lst[j]
            if abs(sm) < abs(minsum):
                minsum = sm
                min_i = i
                min_j = j

    print minsum,lst[min_i],lst[min_j]
'''
# Method 2

def f(lst):
    # Sort the list
    lst.sort()
    new = []
    # Question says the list contains both positive and negative numbers. So not checking the all positive/only negative cases
    ind= None
    for elem in lst:
        if elem > 0:
           ind = lst.index(elem)
           break
    i = ind-1
    j = ind
    min_i = None
    min_j = None
    while i < j and j < len(lst) and i >= 0:
        minsum = None
        sm = lst[i] + lst[j]
        if sm == 0:
           return lst[i],lst[j]
        if sm > 0:
           if minsum is None or abs(sm) < abs(minsum):
               minsum = sm
               min_i = i
               min_j = j
           i = i-1
        if sm < 0:
           if minsum is None or abs(sm) < abs(minsum):
               minsum = sm
               min_i = i
               min_j = j
           j = j +1
    return minsum, lst[min_i], lst[min_j]
f([1,60,-10,70,-80,85])

if __name__ == '__main__':
   assert(f([1,60,-10,70,-80,85])) == (5,-80,85)