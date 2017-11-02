"""
 Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

"""
def isdup(lst):
    x = True
    while x:
        for elem in lst:
            if lst.count(elem) > 1:
                x = False
                break
        if x == True:
            return False
        else:
            return True
if __name__ == '__main__':
    assert (isdup([1,2,3])) == False
    assert (isdup([1, 2, 2])) == True