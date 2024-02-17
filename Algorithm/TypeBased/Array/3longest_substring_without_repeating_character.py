def longest_Substring(String1):
    # "abcabcbb"
    temporary_set = set()
    longestSubstringLength = 0
    count_index = 0
    for index in range(len(String1)):
        while String1[index] in temporary_set:
            temporary_set.remove(String1[count_index])
            count_index += 1

        temporary_set.add(String1[index])
        longestSubstringLength = max(len(temporary_set), longestSubstringLength)

    return longestSubstringLength
print(longest_Substring("loddktdji"))