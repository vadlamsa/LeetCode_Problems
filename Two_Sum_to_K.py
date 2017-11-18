"""Given an array of elements. Find two elements in the array such that their sum is
equal to given element /?
"""
# Method 1: Brute force . Time complexity O(n2)
'''
def f(lst,k):
    for i in range(len(lst)):
        for j in range(1,len(lst)):
            if lst[i] + lst[j] == k:
                print lst[i], lst[j]
                return lst[i],lst[j]
'''

# Method 2: Time complexity O(nlogn). If the list is already sorted then the complexity is O(n)

def f(lst,k):
# sort the list.
    lst.sort()
    i = 0  # Low index
    j = len(lst) - 1  # High index
    temp = None
    while i < j :
        temp = lst[i] + lst[j]
        if temp == k:
            return lst[i],lst[j]
        elif temp < k:
            i = i + 1
        else:
            j = j - 1

if __name__ == '__main__':
    assert(f([2,1,3,5],5)) == (2, 3)
    assert (f([2, 1], 3)) == (1, 2)
