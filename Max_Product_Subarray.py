"""
 Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.


"""
def max_product(l):
    pro = None
    res= []
    for i in range(len(l)-1):
        if pro is None:
            pro = l[i]*l[i+1]
            res = [l[i],l[i+1]]
        elif l[i]*l[i+1] > pro:
            pro = l[i]*l[i+1]
            res = [l[i],l[i+1]]
    return res

if __name__ == '__main__':
     assert (max_product([2, 3, -2, 4])) == [2, 3]
     assert (max_product([1,4,2,3])) == [4,2]
     assert (max_product([-2,4,2,3])) == [4,2]
     assert (max_product([-2,4,-2,3])) == [-2,3]