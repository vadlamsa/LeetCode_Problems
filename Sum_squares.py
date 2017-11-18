"""
Given an array A of  elements. Find three elements such
that	A[i]^2+ A[j]^2 = k^2?
"""
# Method 1 : Brute force . Time complexity of O(n2)

def f(lst,k):
    for i in range(len(lst)):
        for j in range(1,len(lst)):
            if lst[i]**2 + lst[j]**2 == k**2:
                print lst[i], lst[j]
                return lst[i],lst[j]

# Method 2 : Time complexity O(nlogn)

def f(lst,k):
# sort the list.
    lst.sort()
    i = 0  # Low index
    j = len(lst) - 1  # High index

    while i < j :
        temp = lst[i]**2 + lst[j]**2
        if temp == k**2:
            return lst[i],lst[j]
        elif temp < k**2:
            i = i + 1
        else:
            j = j - 1

if __name__ == '__main__':
   assert(f([2,4,9,3,5],5)) == (3, 4)
   assert (f([3, 0,3],3)) == (0, 3)
