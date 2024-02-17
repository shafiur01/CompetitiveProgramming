# from collections import defaultdict
#
# class Solution:
#     def groupAnagrams(self, strs):
#         res = defaultdict(list)
#
#         for word in strs:
#             count = [0]*26
#
#             for letter in word:
#                 count[ord(letter)-ord("a")] += 1
#
#             res[tuple(count)].append(word)
#
#         return res.values()
#
#     list1 = ["eat", "tea", "tan", "nat", "bat"]
#     print(groupAnagrams(list))

# myDictionary = dict(masfe="001", mahi="002", sampad="003", rafsan=4)
# print(myDictionary)
# print(type(myDictionary), "\n")
# print(myDictionary['rafsan'])
# print(type(myDictionary['rafsan']), "\n")
# print(myDictionary['masfe'])
# print(type(myDictionary['masfe']), "\n")
# print(myDictionary.keys())
# print(myDictionary.values(), "\n")
# print(myDictionary.get('masfe'))
# print(myDictionary.pop('rafsan'))
# # the next line clears the whole dictionary
# # print(myDictionary.clear())
# # print(myDictionary)
#
# print(myDictionary.items())
# print(myDictionary.update({'ozayer':'004'}))
# print(myDictionary)
# x = myDictionary.copy()
# print(x)
#
# for x, y in myDictionary.items():
#     print(x, " ", y)
#
# myDictionary['mahi']='009'
# print(myDictionary)
#
# del myDictionary['mahi']
# print(myDictionary)


# alphabet = [0] * 26
# print(alphabet.__str__())
# print(type(alphabet.__str__()))
# print(alphabet)
# print(type(alphabet))

# : List[str]) -> List[List[str]]
# class AnagramSolution:
#     def __init__(self, name):
#         self.name = name
#
#     def groupAnagrams(self, strs):
#         def convert(word):
#             # i'm making an array of 0 of length 26
#             # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#             alphabet = [0] * 26
#
#             # checking which letter is currently in checking
#             # for word tea it will be
#             # [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
#             for letter in word:
#                 indexOfLetter = ord(letter) - ord('a')
#                 alphabet[indexOfLetter] += 1
#             return tuple(alphabet)
#
#         dictionary = dict()
#         # list1 = ["eat", "tea", "tan", "nat", "bat"]
#         for word in strs:
#             code = convert(word)
#             if code in dictionary:
#                 dictionary[code].append(word)
#             else:
#                 dictionary[code] = [word]
#
#         result = []
#         for values in dictionary.values():
#             result.append(values)
#         return result


class AnagramSolution:
    def __init__(self, name):
        self.name = name

    def groupAnagrams(self, strs):

        def convert(word):
            alphabet = [0]*26

            for letter in word:
                position = ord('a')-ord(letter)
                alphabet[position] += 1
            return alphabet

        dictionary = dict()
        for words in strs:
            word_key = convert(words)
            if word_key in dictionary:
                dictionary[word_key].add(words)
            else:
                dictionary[word_key] = words


if __name__ == "__main__":
    currentDict = AnagramSolution("Shafiur")
    list1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(currentDict.groupAnagrams(list1))
