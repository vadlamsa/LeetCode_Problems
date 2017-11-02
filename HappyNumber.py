"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of
the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle
which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
"""
def happy(n):
    lst =[]
    sqlst =[]
    sumlst = None
    while sumlst != 1:
      while n >= 10:
        digit = n % 10
        lst.append(digit)
        n = n//10
      lst.append(n)
      for elem in lst:
         newelem = elem**2
         sqlst.append(newelem)
      sumlst = sum(sqlst)
    if sumlst == 1:
        return True
    else:
        return False

if __name__ == '__main__':
    assert (happy(10)) == True
    assert (happy(20)) == False




