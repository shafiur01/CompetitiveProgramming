from collections import defaultdict

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    # we'll make a dictionary where it will contain the key tuple of the letters as key and a list for values
    # the key tuple will help us to identify which combination of letters a new word has, if they are anagrams then
    # the key tuple will match like (aelpp) : [[apple], [papel], [apepl]]
    # but for finding the tuple here we can make an array of letters of (a-z) and traversing through a word will give
    # us the tuple, but here making an array with 26 letter is a lot of manual work, so we can use ord(letter)-ord(a)
    # which gives us the position of the letter in the array, and it also fulfils the same objective we had for letter
    # tuple.
    # now when we're done going over the list of string we will get all the anagrams contained for each tuple value
    # we can just return the values of the dictionary in a list that will give us a list of anagram list

    helperDictionary = defaultdict(list)

    for word in strs:
        helperList = [0]*26
        for letter in word:
            helperList[ord(letter)-ord('a')] += 1

        helperDictionary[tuple(helperList)].append(word)

    return helperDictionary.values()




print(groupAnagrams(["hello", "olehl", "appl", "plap", "two", "owt", "tow"]))