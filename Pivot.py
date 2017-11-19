"""
Given a sorted array of  integers that has been rotated an unknown number of times,
give a O(logn) algorithm that finds an element in the array.
Example: Find 5 in array [15, 16, 19, 20, 25, 1, 3,	4,5,7,10,14]
Output: 8 (the index of 5 in the array)
"""
# The linear search method has O(n) complexity. This has O(log n) time complexity
def BinarySearchRotated(l,start,finish,data):
    if start > finish:
        return -1
    mid = (start+ finish)//2

    if data == l[mid]:
        return mid
    elif l[start] <= l[mid]:
    # This means the first half is the sorted half
        if data >= l[start] and data < l[mid]:
            return BinarySearchRotated(l,start,mid-1,data)
        else:
            return BinarySearchRotated(l,mid+1,finish,data)
    else:
    # If finish half is sorted
        if data > l[mid] and data <= l[finish]:
            return BinarySearchRotated(l, mid + 1, finish, data)
        else:
            return BinarySearchRotated(l, start, mid - 1, data)


x=BinarySearchRotated([15,16,19,20,25,1,3,4,5,7,10,14],0,11,5)
print x



