"""
Leetcode: 9
Given an integer x, return true if x is a
palindrome and false otherwise.
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

class Solution:
    def countSubstrings(self, s: int):  # -> int:
        # # first solution
        # if i<0:
        #     return False
        # if len(str(i)) == 0:
        #     return True
        # if len(str(i)) % 2 == 0:
        #     index1 = len(str(i))//2
        #     firstHalf = int(str(i)[:index1])
        #     secondHalf = int(str(i)[index1:][::-1])
        #     if firstHalf == secondHalf:
        #         return True
        #     else:
        #         return False
        # else:
        #     index1 = len(str(i)) // 2
        #     firstHalf = int(str(i)[:index1])
        #     secondHalf = int(str(i)[index1+1:][::-1])
        #     if firstHalf == secondHalf:
        #         return True
        #     else:
        #         return False


        # second solution
        return str(x) == str(x)[::-1]

if __name__ == "__main__":
    binarySearch = Solution()
    # notice the array is sorted
    integer = 1211
    print(binarySearch.countSubstrings(integer))
