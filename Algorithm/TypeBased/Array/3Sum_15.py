"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

class Solution:
    def threeSum(self, nums): #-> List[List[int]]:
        returnList = []
        nums.sort()

        for index, element in enumerate(nums):
            if index > 0 and nums[index] == nums[index-1]:
                continue

            left, right = index+1, len(nums)-1
            while left < right:
                sums = nums[index] + nums[left] + nums[right]
                if sums == 0:
                    returnList.append([element, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif sums < 0:
                    left += 1
                elif sums > 0:
                    right -= 1
        return returnList
        ## this method is correct, but it has bad time and space complexities that's why it gives runtime error in LC
        # returnList = []
        # helperList = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         initialSum = nums[i] + nums[j]
        #         required = -initialSum
        #         if required in nums[j + 1:]:
        #             innerList = [nums[i], nums[j], required]
        #             x = set(innerList)
        #             if x not in helperList:
        #                 helperList.append(x)
        #                 returnList.append(innerList)
        # return returnList


if __name__ == "__main__":
    x = Solution()
    list1 = [-1,0,1,2,-1,-4]
    print(x.threeSum(list1))