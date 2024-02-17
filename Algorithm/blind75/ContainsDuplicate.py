class Solution(object):

    def __init__(self, name):
        self.name = name

    def containsDuplicate(self, nums):

        """
        :type nums: List[int]
        :rtype: bool
        """
        set1 = set()
        for digit in nums:
            if digit in set1:
                return True
            else:
                set1.add(digit)
        return False

        # dictionary = dict()
        # for i in range(len(nums)):
        #     if i == 0:
        #         dictionary[nums[i]] = 1
        #     elif nums[i] in dictionary.keys():
        #         return True
        #     else:
        #         dictionary[nums[i]] = 1
        #         continue
        # return False


if __name__ == "__main__":
    name1 = "Shafiur"
    duplicate = Solution(name1)
    array = [1,2,5,3,4,5,6]
    print(duplicate.containsDuplicate(array))
