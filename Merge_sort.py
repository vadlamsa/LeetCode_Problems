def merge_sort(lst):
    # split the list
 if len(lst) > 1:
    mid = len(lst)//2
    left = lst[:mid]
    right = lst[mid:]
    i = 0
    j = 0
    k = 0
    merge_sort(left)
    merge_sort(right)
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst[k] = left[i]
            i = i+1
            k = k+1
        else:

            lst[k] = right[j]
            j = j+1
            k = k+1
    while i < len(left):
        lst[k] = left[i]
        i = i+1
        k = k+1
    while j < len(right):
        lst[k] = right[j]
        j =j+1
        k = k+1

    # returning the merged list
 return lst

lst = [21, 1, 26, 45]
merge_sort(lst)
print(lst)
if __name__ == '__main__':
    assert(merge_sort([54,26,93,17,77,31,44,55,20])) == [17, 20, 26, 31, 44, 54, 55, 77, 93]
    assert (merge_sort([21, 1, 26, 45])) == [1, 21, 26, 45]
    assert(merge_sort([21])) == [21]