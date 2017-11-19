# coding=utf-8
"""
Let A be an array of distinct n integers. Suppose A has the following property: there
exists an index 1 ≤ k ≤ n such that A[1], . . A[k] is an increasing sequence and A[k+1], . . . , A[n]
is a decreasing sequence. Design and analyze an efficient algorithm for finding k.
"""
# List index method uses O(n) complexity, this approach uses O(logn) which is better as it becomes asymptotic
def f(l):
    first = l[0]
    n = len(l)
    last = l[n-1]
    while first <= last:
    # If only 1 elem in list
      if n == 1:
        return l[0]
    # If there are 2 elems in the list
      elif n == 2:
        return max(l)
    # if there are 3 or more elems in the list
      else:
        mid = (first + last)//2
        if l[mid] > l[mid-1] and l[mid] > l[mid+1]:
            return l[mid]
        elif l[mid] > l[mid-1] and l[mid] < l[mid+1]:
            first = mid + 1
        elif  l[mid] < l[mid-1] and l[mid] > l[mid+1]:
            last = mid -1


def f(l):
    first = l[0]
    n = len(l)
    last = l[n-1]
    mid = (first + last) // 2
    while mid <= last:
    # If only 1 elem in list
      if n == 1:
        return l[0]
    # If there are 2 elems in the list
      elif n == 2:
        return max(l)
    # if there are 3 or more elems in the list
      else:

        if l[mid] > l[mid-1] and l[mid] > l[mid+1]:
            return l[mid]
        elif l[mid] > l[mid-1] and l[mid] < l[mid+1]:
            mid = mid + 1
        elif  l[mid] < l[mid-1] and l[mid] > l[mid+1]:
            mid = mid -1

if __name__ == '__main__':
    assert(f([-9,-5,-1,1,2,8,7])) == 8
    assert (f([-9, -5, -1, 1, 2, 8, 7,1])) == 8
    assert (f([-9, -5, -1, 1, 2, 8])) == 8