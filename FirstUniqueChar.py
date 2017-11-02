"""
 Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

"""
def nonrepeat(s):
    for elem in s:
        if s.count(elem) == 1:
            return s.index(elem)


if __name__ == '__main__':
    assert (nonrepeat('loveleetcode')) == 2
    assert (nonrepeat('leetcode')) == 0
