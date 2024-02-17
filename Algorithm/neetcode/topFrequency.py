# # solution for sorted list
#
# class Solution(object):
#     def __init__(self, name):
#         self.name = name
#
#     def topKFrequent(self, nums, k):
#         # nums = [1, 1, 1, 2, 2, 3], k = 2
#         lengthOfNums = len(nums)
#         dictionary = dict()
#         for i in range(1, lengthOfNums+1):
#             dictionary[i] = []
#         # print(dictionary)
#
#         count = 0
#         for i in range(len(nums)):
#             if len(nums) == 1:
#                 dictionary[1].append(nums[0])
#                 break
#             if i == 0:
#                 count += 1
#                 continue
#             if nums[i-1] == nums[i]:
#                 count += 1
#                 if i == len(nums)-1:
#                     dictionary[count].append(nums[i])
#             else:
#                 if count in dictionary:
#                     dictionary[count].append(nums[i-1])
#                     count = 1
#                 if i == len(nums)-1:
#                     dictionary[count].append(nums[i])
#                 continue
#
#         output = []
#         for i in range(len(dictionary), 0, -1):
#             if len(output) == k:
#                 break
#             if len(output) < k:
#                 if len(output) == 1:
#                     if len(dictionary[i]) >= 2:
#                         output.append(dictionary[i][0])
#                         break
#                 if len(dictionary[i]) >= 2:
#                     output.extend(dictionary[i][0:2])
#                     break
#                 if len(dictionary[i]) == 1:
#                     output.append(dictionary[i][0])
#
#         return output
#
#
# if __name__ == "__main__":
#     name = "Shafiur"
#     topkelement = Solution(name)
#     num = [3, 0, 1, 0]
#     k = 2
#     print(topkelement.topKFrequent(num, k))


# # solution -1
# class Solution(object):
#     def __init__(self, name):
#         self.name = name
#
#     def topKFrequent(self, nums, k):
#         count = {}
#
#         # nums = [1, 1, 1, 2, 2, 3, 4], k = 2
#         freq = [[] for i in range(len(nums)+1)]
#
#         for n in nums:
#             # {1:3, 2:2 , 3:1, 4:1}
#             count[n] = 1 + count.get(n, 0)
#         print(count)
#
#         for n, c in count.items():
#             # [[], [3, 4], [2], [1], [], [], [], []]
#             freq[c].append(n)
#
#         most = []
#         for i in range(len(freq)-1, 0, -1):
#             for n in freq[i]:
#                 most.append(n)
#                 if(len(most) == k):
#                     return most
#
#
# if __name__ == "__main__":
#     name = "Shafiur"
#     topkelement = Solution(name)
#     num = [3, 0, 1, 0]
#     k = 2
#     print(topkelement.topKFrequent(num, k))


# # solution 2
# class Solution(object):
#     def __init__(self, name):
#         self.name = name
#
#     def topKFrequent(self, nums, k):
#         freq = {}
#         result = []
#
#         for i in nums:
#             if i in freq:
#                 freq[i] = 1 + freq[i]
#             else:
#                 freq[i] = 1
#         print(freq)
#
#         for i in range(k):
#             maxValue = max(freq, key=freq.get)
#             result.append(maxValue)
#             freq.pop(maxValue)
#         return result
#
#
# if __name__ == "__main__":
#     name = "Shafiur"
#     topkelement = Solution(name)
#     num = [2, 3, 0, 1, 0, 0, 2,]
#     k = 2
#     print(topkelement.topKFrequent(num, k))



# # solution 3
import collections


class Solution(object):
    def __init__(self, name):
        self.name = name

    def topKFrequent(self, nums, k):
        map = collections.defaultdict(lambda: 0)
        for i in nums:
            map[i] += 1
        newmap = sorted(map.items(), key=lambda x: x[1])
        arr = []
        for i in range(k):
            arr.append(newmap[i][0])
        return arr


if __name__ == "__main__":
    name = "Shafiur"
    topkelement = Solution(name)
    num = [2, 3, 0, 1, 0, 0, 2,]
    k = 2
    print(topkelement.topKFrequent(num, k))