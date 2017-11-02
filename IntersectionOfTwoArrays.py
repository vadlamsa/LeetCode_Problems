"""
 Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:

    Each element in the result must be unique.
    The result can be in any order.

"""
def rem(l1,l2):
    ans =[]
    for num in l1:
        if num in l2 and num not in ans:
            ans.append(num)
    return ans

if __name__ == '__main__':
    assert (rem([1,2,2,1],[2,2])) == [2]
    assert (rem([1, 3, 1], [3])) == [3]