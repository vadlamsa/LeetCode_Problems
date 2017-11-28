"""
Given a string, find the  longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc".

"""
def f(s):
    n = len(s)
    seen = []
    max_seen = []
    # eliminate the case of the entire string having the same letter
    if list(set(s)) == list(s[0]):
        return s[0]
    for i in range(n-1):
        if s[i] != s[i+1] and s[i] not in seen:
            seen.append(s[i])
            if len(seen) > len(max_seen):
                max_seen = seen
        if s[i] == s[i-1] and s[i] in seen:
            seen = [s[i]]
    return ''.join(max_seen)

print f('abcabcbb')
print f('bbbbb')
print f('pwwkew')
print f('geeksforgeeks')


if __name__ == '__main__':
       assert(f('abcabcbb')) == 'abc'
       assert(f('bbbbb')) == 'b'
       assert(f('pwwkew')) == 'wke'
       assert(f('geeksforgeeks')) == 'eksforg'