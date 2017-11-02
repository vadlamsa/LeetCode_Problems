"""
 Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
"""
def intsum(n):
    while n>9:
        quo = n//10
        rem = n % 10
        n = quo + rem
    return n

if __name__ == '__main__':
    assert (intsum(38)) == 2
    assert (intsum(10)) == 1
