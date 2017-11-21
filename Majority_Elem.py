"""
An element is a majority if it appears more than n/2 times. Give and algorithm takes
an array of n element as argument and identifies a majority (if it exists). Don't use built in count function.
"""
# Method 1: Dictionary. O(n) complexity

def f(l):
    cnt = 0
    d = {}
    for elem in l:
        if elem in d:
            d[elem] = d[elem] + 1
        else:
            d[elem] = 1
    for k,v in d.items():
        if v > len(l)//2:
            return k

x=f([1,2,2,0])
print x

# Method 2 : Brute Force. O(n2) time complexity
def g(l):
    cnt = 0
    maj_cnt = len(l)//2
    for i in range(len(l)):
        for j in range(1,len(l)):
            if l[i] == l[j] and i != j:
                cnt = cnt+1
        if cnt > maj_cnt:
            maj_cnt = cnt
            break
    return l[i]

x=g([1,2,2,2,1])
print x

# Method 3: Sort and scan. Time complexity O(nlogn)
# no matter what value the majority element has in relation to the rest of the array, the value at [n/2]
# index will always be the majority element.

def f(l):
    l.sort()
    return(l[len(l)//2])

x = f([1,2,2,2,2,3])
print x

# Method 4: Moore's Algorithm. Time complexity O(n)
# 1st find the element that appears maximum number of times in a list. Then check if that element occurs more than n/2 times.
# n being the array length

def m(l):
    maj_index = 0
    cnt = 1
    for i in range(len(l)):
        if l[maj_index] == l[i]:
            cnt = cnt + 1
        else:
            cnt = cnt -1
    # Whenever the count hits zero, change maj_index to the then running element index. After we keep on deducting the count for non-similar
    # elements, the element which has a count of 1 at the end of the is the number which occures maximum number of times.
        if cnt == 0:
            maj_index = i
            cnt = 1
    # Doing a scan to check if the count of the elem occuring maximum number of times is greater than n/2
    for i in range(len(l)):
        if l[i] == l[maj_index]:
            cnt = cnt + 1
    if cnt > len(l)//2 :
        return l[maj_index]
    else:
        return -1



if __name__ == '__main__':
    assert(m([2,2,3,5,2,2,6])) == 2
    assert (m([2, 2, 3,3,2,2,6,2])) == 2
