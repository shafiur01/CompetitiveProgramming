from collections import Counter


class Solution:
    def majorityElement(self, nums):  # -> int:
        count_dict = Counter(nums)
        print(count_dict)
        majority_key = max(count_dict, key=lambda x: count_dict[x])
        print(majority_key)
        max_value = count_dict[max(count_dict, key=lambda x: count_dict[x])]
        print(max_value)
        # return majority_key


if __name__ == "__main__":
    x = Solution()
    list1 = [2,2,1,1,1,2,2,3,3,3,3,5,5,5,5,5]
    print(x.majorityElement(list1))