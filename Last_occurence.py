"""
Give a sorted array of n elements, possibly with duplicates, find the index of the
last occurrence of a number in O(log n) time
"""
# Recursion uses O(logn) time.
def last_occ(l,start,end,target):
    if start <= end:
        mid = (start+end)//2

        # target < l[mid+1] this condition makes sure that the occurence of the elem is the last occurence.
        # If it were not the last occurence then target = l[mid+1]. So to filter out that case we have the  former condition.
        # And if end is equal to mid then the question of any element following the end element does not even arise.
        # That case is handled by if end == mid condition

        if (end == mid and l[mid] == target) or (l[mid] == target and target < l[mid+1]):
            return mid
        # Giving preference to right half of the array because we need the last occurence of the element.
        # If the mid element is less than the target elem, then, for sure target lies between the end element and the (mid+1)th elem
        # both inclusive
        elif (l[mid] <= target):
            return last_occ(l,mid+1,end,target)
        else:
        # If the mid elem is greater than the target elem then certainly the target must lie between the (mid-1)th elem
        # and start elem both inclusive
            return last_occ(l,start,mid-1,target)
    else:
        return -1

if __name__ == '__main__':
    assert(last_occ([3, 4, 5, 6, 6, 7],0,5,6)) == 4
    assert (last_occ([3, 4, 5, 6, 6, 7], 0, 5, 4)) == 1
    assert (last_occ([3, 4, 5, 6, 6, 7], 0, 5, 9)) == -1