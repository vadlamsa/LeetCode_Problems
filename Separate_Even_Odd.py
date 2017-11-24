"""
Given an array [], write a function that segregates even and odd numbers. The functions should
put all even numbers first, and then odd numbers. The even and odd numbers can appear i nay order internally.
Input = {12, 34, 45, 9, 8, 90, 3}
Output = {12, 34, 90, 8, 9, 45, 3}


"""
# Time complexity O(n)

def f(l):
    left = 0
    right = len(l)-1
    while (left < right):
      #  if elem is even then increment the left index
        while l[left] % 2 == 0 and left < right:
            left = left +1
    # if elem is odd then decrement the right index
        while l[right] % 2 == 1 and left < right:
            right = right - 1
    # whenever the loop a point such that left index gets an odd value
    # or right index gets an even element then swap the 2 elements.
    # 'left < right' is to see that we dont back swap the same elements once again
        if left < right:
            l[left],l[right] = l[right],l[left]
            left = left +1
            right = right -1
    return l
x = f([12,34,45,9,8,90,3])
print x

if __name__ == '__main__':
    assert f([12,34,45,9,8,90,3]) == [12, 34, 90, 8, 9, 45, 3]