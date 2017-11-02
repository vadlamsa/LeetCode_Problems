"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],Return:
[ ["ate", "eat","tea"],  ["nat","tan"],["bat"]
]
"""
def grup_anagram(lst):
   new= []
   result = {}
   # Creating a new list where each word in the list is sorted. the whole list is not sorted
   for s in lst:
       new.append((" ").join(sorted(s)))
   # Creating a dictionary where keys are words from original list and values are the sorted words from new list
   d = {}
   for i in range(len(new)):
       d[lst[i]] = new[i]
   # The key in dictionary 'd' is the value in dictionary 'result'

   for key in d:
       if d[key] in result:  # Here 'd[key]' ,'key' represent the key and value respectively in dictionary 'result'
           result[d[key]].append(key) # If key is already present thn to that key add the value
       else:
           result[d[key]] = [key] # Otherwise create the key and add the value
   return result.values()

if __name__ == '__main__':
    assert (grup_anagram(["eat", "tea", "tan", "ate", "nat", "bat"])) == [['bat'], ['ate', 'tea', 'eat'], ['nat', 'tan']]