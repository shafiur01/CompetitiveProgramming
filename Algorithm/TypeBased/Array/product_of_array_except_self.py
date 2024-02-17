"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

import math
class Solution:
    def productExceptSelf(self, nums): #-> nums[int]:
        lp = 1
        rp = math.prod(nums[1:])
        x = []
        for i in range(len(nums)):
            if i == 0:
                x.append(rp)
            else:
                lp *= nums[i - 1]
                if nums[i] != 0:
                    rp //= nums[i]
                    x.append(lp*rp)
                else:
                    x.append(math.prod(nums[0:i]) * math.prod(nums[i + 1:]))
        return x

    # import math
    # class Solution:
    #     def productExceptSelf(self, nums: nums[int]) -> nums[int]:
    #         productContainingArray = []
    #         leftProduct = 1
    #         rightProduct = math.prod(nums[1:len(nums) + 1])
    #         for i in range(len(nums)):
    #             if i == 0:
    #                 leftProduct = 1
    #             elif i > 0:
    #                 leftProduct = nums[i - 1] * leftProduct
    #                 if nums[i] == 0:
    #                     rightProduct = math.prod(nums[i + 1:len(nums) + 1])
    #                 else:
    #                     rightProduct = int((rightProduct) / nums[i])
    #             productContainingArray.append(leftProduct * rightProduct)
    #         return productContainingArray


if __name__ == "__main__":
    x = Solution()
    list1 = [-1,1,0,-3,3]
    print(x.productExceptSelf(list1))