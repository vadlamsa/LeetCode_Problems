"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.
"""
def isomorphic(s,t):
    snl =[]
    tnl =[]
    for char in s:
        snl.append(s.count(char))
    for char in t:
        tnl.append(t.count(char))
    if snl == tnl:
        return True
    else:
        return False


if __name__ == '__main__':
    assert(isomorphic('egg','add')) == True
    assert(isomorphic('paper','title')) == True
    assert (isomorphic('foo', 'bar')) == False
