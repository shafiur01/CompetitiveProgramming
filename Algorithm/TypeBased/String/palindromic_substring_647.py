"""
Leetcode: 647
Given a string s, return the number of palindromic substrings in it. A string is a
alindrome when it reads the samebackward as forward. A substring is a contiguous sequence
of characters within the string.

Example
1:

Input: s = "abc"
Output: 3
Explanation: Three
palindromic
strings: "a", "b", "c".
Example
2:

Input: s = "aaa"
Output: 6
Explanation: Six
palindromic
strings: "a", "a", "a", "aa", "aa", "aaa".
"""

class Solution:
    def countSubstrings(self, s: str):  # -> int:
        count = 0

        for index in range(len(s)):
            left, right = index, index
            while left >= 0 and right<len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            left, right = index, index+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        return count


if __name__ == "__main__":
    binarySearch = Solution()
    # notice the array is sorted
    string = "aaa"
    print(binarySearch.countSubstrings(string))
