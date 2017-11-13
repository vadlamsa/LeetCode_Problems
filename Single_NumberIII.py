"""
 Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice.
 Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:

    The order of the result is not important. So in the above example, [5, 3] is also correct.
    Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

"""
def f(arr):
    d = {}
    for elem in arr:
        d[elem] = d.get(elem,0)+1
    for i,v in d.items():
        if v >1:
            del d[i]
    return list(d.keys())

if __name__ == '__main__':
    assert (f([1, 2, 1, 3, 2, 5])) == [3,5]
    assert(f([1,2])) == [1,2]