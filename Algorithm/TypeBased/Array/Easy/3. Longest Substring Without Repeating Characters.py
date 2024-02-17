# def lengthOfLongestSubstring(String1: str) -> int:
#     left = 0
#     temp_longest_substring = set()
#     lengthOfLongestSubstring = 0
#
#     for r in range(len(String1)):
#         while String1[r] in temp_longest_substring:
#             temp_longest_substring.remove(String1[left])
#             left = left + 1
#         else:
#             temp_longest_substring.add(String1[r])
#             lengthOfLongestSubstring = max(lengthOfLongestSubstring, len(temp_longest_substring))
#
#     return lengthOfLongestSubstring
#
#
# print(lengthOfLongestSubstring("abcabcbb"))
#
#



def max_difference(arr):
    # n = len(arr)
    # if n < 2:
    #     return -1  # Not enough elements to find a difference
    #
    # min_element = arr[0]
    # max_difference = arr[1] - arr[0]
    #
    # for i in range(1, n):
    #     if arr[i] < min_element:
    #         min_element = arr[i]
    #     else:
    #         diff = arr[i] - min_element
    #         if diff > max_difference:
    #             max_difference = diff


    n = len(arr)
    min_num = arr[0]
    max_difference = -1

    for index in range(n):
        if arr[index] <= min_num:
            min_num = arr[index]
        else:
            diff = arr[index]-min_num
            if diff > max_difference:
                max_difference = diff

    return max_difference


# Example usage:
arr = [2, 15, 17]
result = max_difference(arr)
print("Maximum Difference:", result)
