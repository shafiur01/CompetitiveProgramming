# def lengthOfLongestSubstring(String1: str) -> int:
#     left = 0
#     temp_longest_substring = set()
#     lengthOfLongestString = -1
#
#     for r in range(len(String1)):
#         while String1[r] in temp_longest_substring:
#             temp_longest_substring.remove(String1[left])
#             left += 1
#         else:
#             temp_longest_substring.add(String1[r])
#             lengthOfLongestString = max(lengthOfLongestString, len(temp_longest_substring))
#     return lengthOfLongestString
#
#
# print(lengthOfLongestSubstring("abcabcbb"))


def lengthOfLongestSubstring(String1: str) -> int:
    # finding out the length of the String1 so that we can use it repetitively without using extra function call
    String1_length = len(String1)
    if String1_length < 3:
        return 0

    window_set = set()
    left = 0
    count = 0

    # going over the length of the string
    for i in range(String1_length):
        # while the letter from the string is already in window_set then it removes the current_initial element of the
        # array and increase the left by 1
        while String1[i] in window_set:
            window_set.remove(String1[left])
            left += 1

        # if the length of the window is less than size 3 then we add the current element of the string
        if len(window_set) < 3:
            window_set.add(String1[i])

        # if the size of the window is equal to 3 then we increase the count by 1 and then delete the current left most
        # item from the window_set using and increase the left by 1
        if len(window_set) == 3:
            count += 1
            window_set.remove(String1[left])
            left += 1
    return count


print(lengthOfLongestSubstring("aaabcabcbb"))