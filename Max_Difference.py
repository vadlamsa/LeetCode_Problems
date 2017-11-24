"""
Find the max difference between large number and the small number such that the large number should always cme after the
small number
Ex [2, 3, 10, 6, 4, 8, 1] max diff is 8. (between 10 and 2)
"""
# Method 1: Brute Force. O(n2) time complexity
# Note: We are not finding the max difference between 2 elements in an array.If a[j] < a[i], then max_diff is negative.
# if a[j] - a[i] > max_dif: condition takes care of it
def f(a):
    max_dif = a[1]-a[0]
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[j] - a[i] > max_dif:
                max_dif = a[j]-a[i]
    return max_dif

x = f([3, 2, 10, 6, 4, 8, 1])
print x

# Method 2: O(n) time complexity
# We are keeping track of i)maximum difference found so far
#                         ii) minimum number visited so far
# The important piece of code here is 'max_diff = a[i] - min_elem'

def f(a):
    max_diff = a[1] - a[0]
    min_elem = a[0]
    for i in range(1,len(a)):
        if a[i] - min_elem > max_diff:
            max_diff = a[i] - min_elem
    # Any subtraction will have a maximum result if the element
    # being subtracted from it is minimum
        if a[i] < min_elem:
            min_elem = a[i]
    return max_diff
x = f([3, 2, 10, 6, 4, 8, 1])
print x

# Method 3: Time complexity O(n) . But space complexity O(n)

def f(a):
    diff  =[]
    max_diff = a[0]
    for i in range(len(a)-1):
        diff.append(a[i+1]-a[i])
    for i in range(1,len(diff)) :
        if diff[i-1] > 0:
# This is the main part of the code. Here when we say diff[i-1] we are refereing to the new_diff[i] obtained from the previous iteration.
#We are not refering to the (i-1)th element of the diff array.
            diff[i] = diff[i]+diff[i-1]
        if max_diff < diff[i]:
            max_diff = diff[i]
    return max_diff
x = f([1,2,90,10,100])
print x

# In the above example the diff array is [1,88,-80,90]. When i = 2 , as explained in the previous comment,
# diff[i] = diff[i] + diff[i-1] is not '-80 + 88 = 8' . It should be ' -80 + 89 = 9'. Where 89 is obtained as the new diff[i] from the
# previous iteration, i.e., when i = 1, diff[i] = diff[i] + diff[i-1], diff[1] = diff[1] + diff[0] so diff[1] = 88 + 1 = 89

# Method 4: A  space optimized and less confusing version of the previous method. Time complexity O(n) and space complexity O(1)

def f(a):
    diff = a[1] - a[0]
    cur_sum = diff
    max_sum = cur_sum
# Instead of creating new array, we are updating cur_sum and max_sum
    for i in range(1,len(a)):
        diff = a[i] - a[i-1]
        if cur_sum > 0:
            cur_sum = cur_sum + diff
        else:
            cur_sum = diff
        if cur_sum > max_sum:
            max_sum = cur_sum
    return max_sum

if __name__ == '__main__':
    assert(f[1,2,90,10,100]) == 99
    assert(f[3, 2, 10, 6, 4, 8, 1]) == 8