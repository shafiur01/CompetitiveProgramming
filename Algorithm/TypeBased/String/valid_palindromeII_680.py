class Solution:
    def validPalindrome(self, s: str): #-> bool:
        # second method
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return self.deleteLeft(s, l+1, r) or self.deleteRight(s, l, r-1)
            l += 1
            r -= 1
        return True

    def deleteLeft(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def deleteRight(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True



    #     # first method
    #     """if s == s[::-1]:
    #         return True
    #     else:
    #         left, right = 0, len(s) - 1
    #         count = 0
    #         if self.leftSubtract(count, left, right, s):
    #             return True
    #         else:
    #             return self.rightSubtract(count, left, right, s)
    #
    # def leftSubtract(self, count, left, right, s):
    #     while left < right:
    #         if count <= 1:
    #             if s[left] != s[right]:
    #                 left += 1
    #                 count += 1
    #                 if count > 1:
    #                     return False
    #                 else:
    #                     continue
    #         left += 1
    #         right -= 1
    #     return True
    #
    # def rightSubtract(self, count, left, right, s):
    #     while left < right:
    #         if count <= 1:
    #             if s[left] != s[right]:
    #                 right -= 1
    #                 count += 1
    #                 if count > 1:
    #                     return False
    #                 else:
    #                     continue
    #         left += 1
    #         right -= 1
    #     return True"""


if __name__ == "__main__":
    binarySearch = Solution()
    # notice the array is sorted
    string = "cabac"
    print(binarySearch.validPalindrome(string))






    # # this algorithm below is actually correct but the main problem is this takes a lot of time and it
    # takes up a lot of space. So later I'll generate another algorithm which is more faster and takes less space

    # newString = ""
    # for index in range(len(s)):
    #     newString = s[:index] + s[index+1:]
    #     if newString == newString[::-1]:
    #         return True
    # return False