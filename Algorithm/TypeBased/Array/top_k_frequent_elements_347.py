"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k: int): #-> List[int]:
        map1 = Counter(nums)
        reverseDict = sorted(map1, key=lambda item: map1[item], reverse=True)
        return reverseDict[:k]


if __name__ == "__main__":
    x = Solution()
    list1 = [1, 3, 3, 4, 4, 4, 5, 5, 3]
    print(x.topKFrequent(list1, 2))














    # map = Counter(nums)
    # print(map)
    # reverse_dict = dict(sorted(map.items(), key=lambda item: item[1], reverse=True))
    # list2 = list(reverse_dict.keys())[:k]
    # return list