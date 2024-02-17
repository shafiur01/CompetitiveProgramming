import math


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        productContainingArray = []
        leftProduct = 1
        rightProduct = math.prod(nums[1:len(nums)+1])
        print(rightProduct)
        for i in range(len(nums)):
            if i == 0:
                leftProduct = 1
            elif i>0:
                leftProduct = nums[i-1]*leftProduct
                if nums[i] == 0:
                    rightProduct = math.prod(nums[i+1:len(nums)+1])
                else:
                    rightProduct = int((rightProduct)/nums[i])
            productContainingArray.append(leftProduct*rightProduct)
        return productContainingArray


if __name__ == "__main__":
    productOfArrayExceptIt = Solution()
    array = [-1,1,0,-3,3]
    print(productOfArrayExceptIt.productExceptSelf(array))