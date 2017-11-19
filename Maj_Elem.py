"""
Given an array of numbers. Give an algorithm for finding the element which
appears maximum number of times in the array? Do not use built in count function.
"""
# Method 1: Brute force. Time complexity O(n2)

def f(l):

    maxcnt = None
    maxelem = None
    for i in range(len(l)):
        counter = 0
        for j in range(1,len(l)):
            if l[i] == l[j]:
                counter = counter + 1
            if maxcnt < counter or maxcnt is None:
                maxcnt = counter
                maxelem = l[i]

    return maxelem

# Method 2: Time complexity O(nlogn) because of sorting.


def f(l):
    l.sort()
    maxelem = None
    maxcnt = None
    counter = 1
    for i in range(len(l)-1):
    # Check if the adjacent elems are equal. If equal, increment the counter
        if l[i] == l[i+1]:
            counter = counter + 1
    # Store the incremented value in maxcnt
        if maxcnt < counter or maxcnt is None:
            maxcnt = counter
            maxelem = l[i]
    # Reset the counter to 1 if the adjacent elems are not equal
        if l[i] != l[i+1]:
            counter = 1
    return maxelem

# Method 3: Use python dictionary but it will consume some extra space. But time complexity will come down to O(n). No need to sort

def f(l):
    d ={}
    for elem in l:
        if elem in d:
            d[elem] = d[elem] + 1
        else:
            d[elem] = 1
    m = max(d.values())
    if m == 1:
       return None
    else:
       for key,item  in d.items():
        if item == m:
            return key

if __name__ == '__main__':
    assert(f([1,22,7,9,3,7,3,7])) == 7
    assert (f([7])) == None

