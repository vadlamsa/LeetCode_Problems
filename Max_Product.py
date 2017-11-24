# coding=utf-8
"""
Given an array A of n numbers. Find all pairs of x and y in the array such that
k = x*y. Give an efficient algorithm without sorting.
"""

# Method 1: Brute force. Time complexity O(n2)

def f(a,k):
    res =[]
    for i in range(len(a)):
        for j in range(1,len(a)):
            if a[i]*a[j] == k:
                res.append((a[i],a[j]))
    return res

x = f([10,20,9,40],400)
print x

# Method 2: Time complexity O(n)

def f(a,k):
    d ={}
    ans = []
    for i in range(len(a)):
# In a dictionary insert the element as the key and the quotient as the value
        if k % a[i] == 0:
           d[a[i]] =(k//a[i])
    for k,v in d.items():
        ans.append((k,v))
    return ans
x = f([10,20,9,40],400)
print x