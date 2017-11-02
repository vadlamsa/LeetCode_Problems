"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.
S = [1, 0, -1, 0, -2, 2], and target = 0.

"""

def func(n):
    ans = []
    unique_ans = []
    for i in range(len(n)):
        for j in range(1, len(n)):
            if j != i:
                for k in range(2, len(n)):
                    if k != j and k != i:
                        for m in range(3,len(n)):
                            if m != i and m != j and m!= k:
                                if n[i] + n[j] + n[k] +n[m] == 0:
                                    ans.append((n[i], n[j], n[k],n[m]))
    for i in ans:
        if sorted(i) not in unique_ans:
            unique_ans.append(sorted(i))
    return unique_ans
if __name__ == '__main__':
    assert (func([1, 0, -1, 0, -2, 2])) == [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]