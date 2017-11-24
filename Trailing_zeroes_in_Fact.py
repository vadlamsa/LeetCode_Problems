"""
Find the number of trailing zeroes in n!
"""
# Method 1: Not efficient
# First find the factorial then count the zeroes

def f(n):
     mul = 1
     cnt = 0
     rem  = 0
     while n > 1:
         mul = mul * n
         n = n-1
     print mul
     while mul > 1 and rem == 0:
         rem = mul % 10
         mul = mul//10
         cnt = cnt + 1
     return cnt - 1

# return cnt -1 to prevent the extra cnt that occurs even when there are no trailing zeroes. It exits does not enter the while condition
#  after there are no zeroes left. However, the count does get incremented before exiting the loop


# Method 2: Efficient

def f(n):
    cnt = 0
    i = 5
    quo = n//i
    while quo >= 1:
        quo = n//i
        cnt = cnt+quo
        i = i*5
    return cnt

x = f(100)
print x