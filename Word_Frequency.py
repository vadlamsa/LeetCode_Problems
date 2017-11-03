"""
Write a script to calculate the frequency of each word in a text file words.txt.

For simplicity sake, you may assume:

    words.txt contains only lowercase characters and space ' ' characters.
    Each word must consist of lowercase characters only.
    Words are separated by one or more whitespace characters.

For example, assume that words.txt has the following content:

the day is sunny the the
the sunny is is

"""
fopen = open('words.txt')
freq = {}
for line in fopen:
    words = line.split()
    for word in words:
        freq[word] = freq.get(word,0)+1
for key,value in freq.items():
    print key, value


