"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.
Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""


class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        closestNum = 10**4
        for index in range(len(nums)-2):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            left, right = index+1, len(nums)-1
            while left < right:
                sum1 = nums[index] + nums[left] + nums[right]
                if sum1 == target:
                    return sum1
                elif abs(target - sum1) < abs(target - closestNum):
                    closestNum = sum1
                if sum1 < target:
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                else:
                    right -= 1

        return closestNum


if __name__ == "__main__":
    x = Solution()
    list1 = [-13,592,-501,770,-952,-675,322,-829,-246,657,608,485,-112,967,-30,182,-969,559,-286,-64,24,365,-158,701,
             535,-429,-217,28,948,-114,-536,-711,693,23,-958,-283,-700,-672,311,314,-712,-594,-351,658,747,949,70,888,
             166,495,244,-380,-654,454,-281,-811,-168,-839,-106,877,-216,523,-234,-8,289,-175,920,-237,-791,-976,-509,
             -4,-3,298,-190,194,-328,265,150,210,285,-176,-646,-465,-97,-107,668,892,612,-54,-272,-910,557,-212,-930,
             -198,38,-365,-729,-410,932,4,-565,-329,-456,224,443,-529,-428,-294,191,229,112,-867,-163,-979,236,-227,
             -388,-209,984,188,-549,970,951,-119,-146,801,-554,564,-769,334,-819,-356,-724,-219,527,-405,-27,-759,722,
             -774,758,394,146,517,870,-208,742,-782,336,-364,-558,-417,663,-914,536,293,-818,847,-322,408,876,-823,827,167]
    print(x.threeSumClosest(list1, 7175))