"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 """

class Solution:
    def maxSubArray(self, nums) -> int:
        # at first we'll initialize Sum = first element
        # we also put a left pointer at the start of the array
        # then we continue comparing our current element with the sum, if we see that the any digit is bigger than the sum then we shift the pointer of the subarray there, and also update the sum with that element
        # we also add the elements gradually if the sum is bigger than our current checked elements and store the max sum every time. And when the loop is finished then we return the max sum, which will eventually be the max sum of the subarray
        max_subarray_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            if current_sum < 0:
                current_sum = nums[i]
            else:
                current_sum += nums[i]
            max_subarray_sum = max(max_subarray_sum, current_sum)

        return max_subarray_sum


if __name__ == "__main__":
    x = Solution()
    list1 = [-2,1,-3,4,-1,2,1,-5,4]
    print(x.maxSubArray(list1))