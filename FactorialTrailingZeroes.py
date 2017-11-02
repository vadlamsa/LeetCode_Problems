"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""

def zerotrail(n):
    mul = 1
    # Finding the factorial of the number
    while n > 0:
        mul = mul*n
        n = n-1
        cnt = 0
    # Counting the number of zeroes in the factorial
    while mul > 0:
        if mul % 10 == 0:
         cnt = cnt +1
         mul = mul//10
    return cnt
if __name__ == '__main__':
   assert (zerotrail(10)) == 2
   assert (zerotrail(5)) == 1
   assert (zerotrail(0)) == 0


zerotrail(10)

