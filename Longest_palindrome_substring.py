"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example:
Input: "babad"
Output: "bab"
"""
def f(s):
    i = 0
    j = len(s)-1
    if s == s[::-1]:
        return s
    # if keep i at zero and check if any palindrome comes
    while i<j and j > 1:
        sr = s[i:j]
        print 'sr=',sr,'i=',i,'j=',j
        if sr == sr[::-1]:
            return sr
        else:
            j = j-1
    # Keep j fixed and check increment i
    i = 0
    j = len(s)
    while i<j-1 :
        sr = s[i:j]
        if sr == sr[::-1]:
            return sr
        else:
            i = i +1
    # If palindrome is not found in both the above cases then it is probably in the middle so then keep incrementing i and decrementing j
    i = 0
    j = len(s)
    while i < j :
            sr = s[i:j]
            if sr == sr[::-1]:
                return sr
            else:
                i = i + 1
                j = j -1
print f('forgeeksskeegfor')

if __name__ == '__main__':
    assert(f('cbbd')) == 'bb'
    assert(f('babad')) == 'bab'
    assert(f('cdbb')) == 'bb'
    assert(f('forgeeksskeegfor')) == 'geeksskeeg'
