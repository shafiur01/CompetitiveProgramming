class Solution:
    def removeElement(self, nums, val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)


if __name__ == "__main__":
    x = Solution()
    list1 = [0,1,2,2,3,0,4,2]
    print(x.removeElement(list1, 2))