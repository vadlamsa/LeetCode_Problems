"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
"""
def func(n):
    ans =[]
    unique_ans =[]
    for i in range(len(n)):
        for j in range(1,len(n)):
            if j != i:
              for k in range(2,len(n)):
                  if k != j and k != i:
                     if n[i]+n[j]+n[k] == 0:
                            ans.append((n[i],n[j],n[k]))
    for i in ans:
        if sorted(i) not in unique_ans:
           unique_ans.append(sorted(i))
    return unique_ans

if __name__ == '__main__':
    if assert (func([-1, 0, 1, 2, -1, -4])) == [[-1, 0, 1], [-1, -1, 2]]
