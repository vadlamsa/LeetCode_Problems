"""
Find a triplet that sum to a given value
"""
# Brute force has time complexity of O(n3). It can be reduced to O(n2)

def f(l,target):
    l = sorted(l)
    i = 0
    while i < len(l)-2:
        j = i + 1
        r = len(l) - 1
        while j < r:
            if l[i]+l[j]+l[r] == target:
                return l[i],l[j],l[r]
            elif l[i]+l[j]+l[r] < target:
                j = j+1
            else:
                r = r-1
        i = i + 1

if __name__ == '__main__':
    assert(f([-1, 0, 1, 2, -1, -4],0)) == (-1, -1, 2)



