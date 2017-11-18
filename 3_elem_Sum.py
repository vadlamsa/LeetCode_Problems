"""
Given an array of elements. Find three elements in the array such that their sum is
equal to given element ?
"""

# Brute force would give a time complexity of O(n3).
# Below is an alternate approach

def f(l,target):
    l.sort()
    for k in range(len(l)):
        i = k+1
        j = j = len(l) -1
        while i < j:
            sm =  l[k]+l[i]+l[j]
            if sm == target:
                return l[k],l[i],l[j]
            elif sm < target:
                i = i + 1
            else:
                j = j - 1

if __name__ == '__main__':
    assert(f([2,9,5,7,1],10)) == (1, 2, 7)
    assert (f([2, 9, 5, 7, 1], 15)) == (1, 5, 9)
    assert (f([2, 9, 5, 7, 1], 21)) == (5, 7, 9)