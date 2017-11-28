"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
"""

# Method 1 : Time complexity O(n2)
def f(l,target):
    for i in range(len(l)):
        for j in range(1,len(l)):
           if l[i] + l[j] == target:
               print (i,j)

f([2, 11,7, 15],9)


# Method 2: Time complexity O(nlogn)
def f(l,target):
    l1 = sorted(l)
    n = len(l)
    left = 0
    right = n-1
    while left < right:
       if l1[left] + l1[right] == target:
         return l.index(l1[left]),l.index(l1[right])
       elif l1[left] + l1[right] < target:
          left = left + 1
       else:
          right = right - 1


if __name__ == '__main__':
    assert(f([2, 11,7, 15],9)) == (0,2)
    assert (f([2, 11, 15, 7], 9)) == (0, 3)

    