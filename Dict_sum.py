"""
Write a Python program to sum all the items in a dictionary.
"""
def f(d):
    sm = 0
    for elem in d.values():
        sm = sm + elem
    return sm

if __name__ == '__main__':
    assert(f({1:1,2:2,3:3})) == 6



