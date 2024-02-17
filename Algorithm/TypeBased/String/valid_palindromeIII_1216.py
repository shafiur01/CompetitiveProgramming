"""
Given a string s and an integer k, return true if s is a k-palindrome.
A string is k-palindrome if it can be transformed into a palindrome by removing at most k characters from it.

Example 1:

Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.
Example 2:

Input: s = "abbababa", k = 1
Output: true
"""


class Solution:
    def isValidPalindrome(self, s: str, k: int): # -> bool:
        l, r = 0, len(s)-1
        count = 0
        # while l < r:
        #     if s[l] != s[r]:
        #         # while count <= k:
        #
        #     l += 1
        #     r -= 1
        return True
    # def deleteLeft(self, s, ):


if __name__ == "__main__":
    x = Solution()
    string = "abbdbbacc"
    print(x.isValidPalindrome(string, 2))