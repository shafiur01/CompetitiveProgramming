class Solution:
    def lengthOfLongestSubstring(self, s: str):

        max_character_set = set()
        index_shift = 0
        max_count = 0

        # s = enumeration
        for index in range(len(s)):
            while s[index] in max_character_set:
                max_character_set.remove(s[index_shift])
                index_shift += 1
            max_character_set.add(s[index])
            max_count = max(max_count, len(max_character_set))
        return max_count


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring('abcad'))

# class Solution:
#     def lengthOfLongestSubstring(self, s: str):
#         first_pointer = 0
#         second_pointer = 0
#         max_set = set()
#         max_length = 0
#         while second_pointer < len(s):
#             if s[second_pointer] not in max_set:
#                 max_set.add(s[second_pointer])
#                 second_pointer += 1
#                 max_length = max(max_length, len(max_set))
#                 continue
#             while s[second_pointer] in max_set:
#                 max_set.remove(s[first_pointer])
#                 first_pointer += 1
#             max_set.add(s[second_pointer])
#             second_pointer += 1
#             max_length = max(max_length, len(max_set))
#         return max_length


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring('elongation'))

