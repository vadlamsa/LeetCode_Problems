"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number,
target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.
S = {-1 2 1 -4}, and target = 1
"""
def func(s,l):
    difference =[]
    triplets = []
    uniqtrip = []
    for i in range(len(s)):
        for j in range(1,len(s)):
            for k in range(2,len(s)):
                if i != j and i !=k and j != k:
                       triplets.append((s[i],s[j],s[k]))
    for i in triplets:
        if sorted(i) not in uniqtrip:
           uniqtrip.append(sorted(i))
    for i in uniqtrip:
        difference.append(abs(sum(i)-l))
    return min(difference)

if __name__ == '__main__':
    assert (func([-1,2,1,-4],1)) == 1
