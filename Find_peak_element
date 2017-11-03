# coding=utf-8
"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
"""
# The question says return any peak_elem index but the 1st element and the last element  have only 1 neighbour. If there is any other
# peak_elem in the array I chose to return the other peak_elem
def peak(l):
    peak_elem = None
# If the array has nly 1 element then that is the peak_elem
    if len(l) == 1:
        peak_elem = l[0]
# If the length of array is 2, then we just compare the 2 elements with each other
    if len(l) == 2:
        if l[0] > l[1]:
            peak_elem = l[0]
        else:
            peak_elem = l[1]
# Only when the length of array is 3 and more, an element has 2 neighbours.(Previous neighbour and succeeding neighbour)
    if len(l) > 2:
        for i in range(len(l)):
            if peak_elem is None:
                peak_elem = l[0]

# But even in that case, the 1st element and the last element of the array have only 1 neighbour. So getting rid of those cases first
            if i == 0 and l[i] >= l[i + 1]:
                    peak_elem = l[i]

            if i == 0 and l[i+1] > l[i]:
                    peak_elem = l[i + 1]

            if i == len(l) - 1:
                if l[i] > l[i-1] and l[i] > peak_elem:
                    peak_elem = l[i]

                elif l[i-1] > l[i] and l[i-1] > peak_elem:
                    peak_elem = l[i-1]

# This is just for the middle elements in the array wherein all these elements have 2 neighbours each

            elif i != 0  and l[i] >= l[i + 1] and l[i] >= l[i - 1]:
                if l[i] >= peak_elem:
                    peak_elem = l[i]
    return l.index(peak_elem)

if __name__ == '__main__':
    assert (peak([3,2,1])) == 0
    assert (peak([1,2])) == 1
    assert (peak([2,1])) == 0
    assert (peak([3])) == 0
    assert (peak([3, 2, 1,4])) == 3
    assert (peak([3, 2, 1,7,4])) == 3

