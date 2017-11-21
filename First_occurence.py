"""
Give a sorted array of n elements, possibly with duplicates, find the index of the
first occurrence of a number in O(log n) time
"""
# Recursion uses O(logn) time.
def first_occ(l,start,end,target):
    if start <= end:
        mid = (start+end)//2

        # target > l[mid-1] this condition makes sure that the occurence of the elem is the first occurence.
        # If it were the 2nd occurence then target = l[mid-1]. So to filter out that case we have the last condition.
        # And if start is equal to mid then the question of any element preceeding the start element does not even arise.
        # That case is handled by if start == mid condition

        if (start == mid and l[mid] == target) or (l[mid] == target and target > l[mid-1]):
            return mid
        # Giving preference to left half of the array because we need the 1st occurence of the element.
        # If the mid element is greater than the target elem, then, for sure target lies between the start element and the (mid-1)th elem
        # both inclusive
        elif (l[mid] >= target):
            return first_occ(l,start,mid-1,target)
        else:
        # If the mid elem is less than the target elem then certainly the target must lie between the (mid+1)th elem
        # and end elem both inclusive
            return first_occ(l,mid+1,end,target)
    else:
        return -1



if __name__ == '__main__':
    assert(first_occ([3,4,5,6,6,7],0,5,6)) == 3
    assert (first_occ([3, 4, 5, 6, 6, 7], 0, 5, 4)) == 1
    assert (first_occ([3, 4, 5, 6, 6, 7], 0, 5, 9)) == -1