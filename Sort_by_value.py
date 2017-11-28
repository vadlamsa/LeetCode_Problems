"""
1. Write a Python script to sort (ascending and descending) a dictionary by value
"""
# I will use a list and its count to create a dictionary. l = [1,1,7,3,3,3,4].

def dict_sort(l):
    d ={}
    for elem in l:                             # This process is so common that there is a
        if elem in d:                          # built in method for doing this.
            d[elem] = d[elem] + 1              # d[elem] = d.get(elem,0)+1
        else:
            d[elem] = 1
     # d = {1: 2, 3: 3, 4: 1, 7: 1}
     # If we had to sort be key, the below code is sufficient.
     # print sorted(d.items()). The result would be [(1, 2), (3, 3), (4, 1), (7, 1)]
     # so now exchange the key with the value and then sort
    arr =[]
    for k,v in d.items():
         arr.append((v,k))
    return sorted(arr)


if __name__ == '__main__':
    assert(dict_sort([1,1,7,3,3,3,4])) == [(1, 4), (1, 7), (2, 1), (3, 3)]





