"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and
numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:

        #second solution
        left, right = 0, len(s)-1
        while left<right:
            while not self.isalphanumeric(s[left]):
                left += 1

            while not self.isalphanumeric(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def isalphanumeric(self, c):
        return (
            (ord('A') < ord(c) < ord('Z')) or
            (ord('a') < ord(c) < ord('z')) or
            (ord('0') < ord(c) < ord('9'))
            )

        # newString = ""
        # for i in s:
        #     if i.isalnum():
        #         newString += i.lower()
        #     else:
        #         newString += ""
        # return newString == newString[::-1]


if __name__ == "__main__":
    binarySearch = Solution()
    # notice the array is sorted
    string = "A man, a plan, a canal: Panama"
    print(binarySearch.isPalindrome(string))
