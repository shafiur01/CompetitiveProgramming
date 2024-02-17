class Solution:
    def thirdMax(self, nums:list): # -> int:
        x = set(nums)
        y = sorted(list(x))
        if len(y) >= 3:
            return y[-3]
        else:
            return max(y)


if __name__ == "__main__":
    x = Solution()
    list1 = [3,2,1]
    print(x.thirdMax(list1))