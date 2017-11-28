"""
 Write a python program to find the longest words.
"""
def f(fname):
    maxlen = 0
    maxword = None
    l = 0
    with open(fname) as fileob:
         for line in fileob:
             words = line.split()
             for word in words:
                 l = len(word)
                 if l > maxlen:
                     maxlen = l
                     maxword = word
         print maxword

f('/home/soumya/Desktop/Files_prac_ex/Untitled 1.txt')