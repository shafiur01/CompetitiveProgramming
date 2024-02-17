def isAnagram(string1: str, string2: str):
    if len(string1) == len(string2):
        listOfString2 = list(string2)
        for letter in string1:
            if letter in listOfString2:
                listOfString2.remove(letter)
            else:
                continue
        return len(listOfString2) == 0
    else:
        return False


print(isAnagram("anagram", "nagaram"))
