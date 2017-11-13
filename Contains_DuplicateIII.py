"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference
between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
"""
def f(lst,t,k):
    ans = None

    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if abs(lst[i]-lst[j]) <= t:
              if abs(i-j) <= k:
                ans = True
                break
            else:
                ans = False
    return ans

if __name__ == '__main__':
    assert (f([3,8,10,9],1,1)) == True
    assert (f([3, 8, 1, 9], 1, 1)) == False
    assert (f([1,2],2,1)) == True