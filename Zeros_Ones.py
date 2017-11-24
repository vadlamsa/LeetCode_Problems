# coding=utf-8
"""
We are given an array of 0’s and 1’s in random order. Separate 0’s on left side and 1’s on right side
of the array. Traverse array only once.
Input array = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
Output array = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
"""
def f(l):
    left = 0
    right = len(l)-1
    while left < right:
       # keep incrementing the left index as long as the elem is zero

        while l[left] == 0 and left < right:
            left = left + 1
       # keep decrementing the right index as long as the elem is 1
        while l[right] == 1 and left < right:
             right = right - 1
       # When 1 is encountered in left index and 0 is encountered in right index, then swap.
       # The left < right is to make sure that the same elements dont get reswapped
        if left < right:
            l[left],l[right] = l[right],l[left]
