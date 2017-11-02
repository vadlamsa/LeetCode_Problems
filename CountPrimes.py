"""
Count the number of prime numbers less than a non-negative number, n.
"""

def numprime(n):
    prime =[]
    notprime =[]
    for num in range(1,n+1):
        for i in range(2,num):
            if num % i == 0:
                notprime.append(num)
        if num not in notprime and num !=1:
            prime.append(num)
    return len(prime)

if __name__ == '__main__':
    assert (numprime(2)) == 1
    assert(numprime(10)) == 4
