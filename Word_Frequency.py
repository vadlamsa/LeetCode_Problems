"""
Write a Python program to count the frequency of words in a file.
"""
def f(fname):
    d ={}
    with open(fname) as fileob:
        for line in fileob:
            words = line.split()
            for word in words:
                d[word] = d.get(word,0) +1
        print d

f('/home/soumya/Desktop/Files_prac_ex/Untitled 1.txt')

