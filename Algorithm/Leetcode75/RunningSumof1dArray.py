class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        author: Shafiur Rahman
        """

        # But the inplace array modification seems to be more effective and space saving method since it doesn't create any new array
        # first method
        # sumArray = []
        # # [1,2,3,4]
        # # len = 4
        # #  0, 1, 2, 3
        # for i in range(len(nums)):
        #     if i == 0:
        #         x = nums[i]
        #     else:
        #         x = nums[i]+sumArray[i-1]
        #     sumArray.append(x)
        # return sumArray


        # second method
        # this method is more space conscious and fast
        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                nums[i] = nums[i]+nums[i-1]
        return nums