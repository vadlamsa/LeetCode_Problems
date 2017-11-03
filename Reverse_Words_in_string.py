"""
 Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
"""
# Method 1

def rev(line):
    words = line.split()
    words =words[::-1]
    return ' '.join(words)


# Method 2
def rev(line):
    words = line.split()
    newline = []
    index = len(words)
    while index > 0:
        newline.append(words[index-1])
        index = index -1
    return ' '.join(newline)


if __name__ == '__main__':
     assert (rev('the sky is blue')) == 'blue is sky the'
     assert (rev('one word')) == 'word one'
     assert (rev('1 2 3')) == '3 2 1'