class Solution:
    def longestCommonPrefix(self, list: [str]):
        # ["flower", "flow", "flight"]
        dict1 = dict()
        list.sort()
        shortest_suffix = ""
        min_word_length = min(list)
        print(min_word_length)
        # for i in range(len(list)):
        #     for letter in list[i]:
        #


if __name__ == '__main__':
    X = Solution()
    list1 = ["flower", "flow", "flight"]
    X.longestCommonPrefix(list1)
