"""
Write a Python program to read a file line by line store it into an array.
"""
def f(fname):
    store_array = []
    with open(fname) as fileob:
        for line in fileob:
            store_array.append(line)
    print store_array


f('/home/soumya/Desktop/Files_prac_ex/Untitled 1.txt')