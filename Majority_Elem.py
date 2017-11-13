# coding=utf-8
"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
The algorithm should run in linear time and in O(1) space.
"""
def f(lst):
    n = len(lst)//3
    d ={}
    
    # Since there isn't a for loop inside of another, after ignoring the lower order terms the time complexity is linear

    for elem in lst:
        d[elem] = d.get(elem,0)+1
    for k,v in d.items():
        if v <= n:
            del d[k]
    return d.keys()

if __name__ == '__main__':
    assert (f([1,1,2])) == [1]
    assert (f([1, 3, 2])) == []
    assert(f([1,1,2,3,4,5])) == []


