"""
Give a sorted array of n elements, possibly with duplicates, find the number of occurences of an element in O(logn) time complexity.
Note: The built in count method uses O(n) time complexity
"""
# Brute Force. Time complexity O(n)
'''
def f(l,target):
    cnt = 0
    for elem in l:
        if elem == target:
           cnt = cnt+1
    return cnt
'''
# Method 2: Time complexity O(logn+logn) = O(logn)
def f(l,target):
    def last_occ(l, start, end, target):
        if start <= end:
            mid = (start + end) // 2

            # target < l[mid+1] this condition makes sure that the occurence of the elem is the last occurence.
            # If it were not the last occurence then target = l[mid+1]. So to filter out that case we have the  former condition.
            # And if end is equal to mid then the question of any element following the end element does not even arise.
            # That case is handled by if end == mid condition

            if (end == mid and l[mid] == target) or (l[mid] == target and target < l[mid + 1]):
                return mid
            # Giving preference to right half of the array because we need the last occurence of the element.
            # If the mid element is less than the target elem, then, for sure target lies between the end element and the (mid+1)th elem
            # both inclusive
            elif (l[mid] <= target):
                return last_occ(l, mid + 1, end, target)
            else:
                # If the mid elem is greater than the target elem then certainly the target must lie between the (mid-1)th elem
                # and start elem both inclusive
                return last_occ(l, start, mid - 1, target)
        else:
            return -1

    def first_occ(l, start, end, target):
        if start <= end:
            mid = (start + end) // 2

            # target > l[mid-1] this condition makes sure that the occurence of the elem is the first occurence.
            # If it were the 2nd occurence then target = l[mid-1]. So to filter out that case we have the last condition.
            # And if start is equal to mid then the question of any element preceeding the start element does not even arise.
            # That case is handled by if start == mid condition

            if (start == mid and l[mid] == target) or (l[mid] == target and target > l[mid - 1]):
                return mid
            # Giving preference to left half of the array because we need the 1st occurence of the element.
            # If the mid element is greater than the target elem, then, for sure target lies between the start element and the (mid-1)th elem
            # both inclusive
            elif (l[mid] >= target):
                return first_occ(l, start, mid - 1, target)
            else:
                # If the mid elem is less than the target elem then certainly the target must lie between the (mid+1)th elem
                # and end elem both inclusive
                return first_occ(l, mid + 1, end, target)
        else:
            return -1
    return last_occ([3,4,5,6,6,7],0,5,6) - first_occ([3,4,5,6,6,7],0,5,6) +1

x=f([3,4,5,6,6,7],6)
print x
if __name__ == '__main__':
   assert(f([3, 4, 5, 6, 6, 7],6)) == 2


# Line 61 if I use l,start , end and target instead , it gives error