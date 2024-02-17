'''
Given a string s, return the longest
palindromic

substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ""  # eroabacabaof
        length = 0
        # here we're traversing the whole array
        for index in range(len(s)):
            left, right = index, index

            # here we're checking both left and right of an element to check if there is any palindrome feature and
            # if there is then we keep track of it and update the 'palindrome' string above with the new string portion
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > length:
                    length = right - left + 1
                    palindrome = s[left:right + 1]
                left -= 1
                right += 1

            # this is an edge case for even number of letters in the palindrome, it's very important too
            left, right = index, index + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > length:
                    length = right - left + 1
                    palindrome = s[left:right + 1]
                left -= 1
                right += 1
        return palindrome


if __name__ == "__main__":
    x = Solution()
    string1 = "eroabacabaof"
    print(x.longestPalindrome(string1))