"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""

class Solution:
    def twoSum(self, numbers, target: int): #-> List[int]:

        # dictionary method
        """
        differenceMap = dict()
        for index, element in enumerate(numbers):
            diff = target-numbers[index]
            if diff in differenceMap.keys():
                return [index+1, differenceMap[element]+1]
            else:
                differenceMap[element] = index
        """

        # two pointers method, it is very effective when we're solving any sum problems related to the array
        # here we'll have two pointers in the left-index of the array and a right pointer at the end index of the array
        # So whenever we'll find that array[left]+array[right] < 0 then :--> left-pointer+1, and when
        # array[left]+array[right] > 0 then :--> right-pointer-1, so this trick ensures less space and less traversal

        left, right = 0, len(numbers)-1

        while left < right:
            currentSum = numbers[left] + numbers[right]
            if currentSum == target:
                return [left+1, right+1]

            elif currentSum < target:
                left += 1
                continue
            elif currentSum > target:
                right -= 1
                continue


if __name__ == "__main__":
    x = Solution()
    list1 = [-1,0]
    print(x.twoSum(list1, -1))