"""
 Write a Python program to count the number of lines in a text file.
"""
def f(fname):
    cnt = 0
    with open(fname) as fileob:
        for line in fileob:
            cnt = cnt +1

        print cnt

f('/home/soumya/Desktop/Files_prac_ex/Untitled 1.txt')