"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.
"""

def f(s):
    n = len(s)
    l = 0
    seen = []
    max_len = 0
    # eliminate the case of the entire string having the same letter
    if list(set(s)) == list(s[0]):
        return 1
    for i in range(n-1):
        if s[i] != s[i+1] and s[i] not in seen:
            l = l +1
            seen.append(s[i])
            if l > max_len:
                max_len = l
        if s[i] == s[i-1] and s[i] in seen:
            l = 1
            max_len = max_len+1
    return max_len
if __name__ == '__main__':
       assert(f('abcabcbb')) == 3
       assert(f('bbbbb')) == 1
       assert(f('pwwkew')) == 3
       assert(f('geeksforgeeks')) == 7