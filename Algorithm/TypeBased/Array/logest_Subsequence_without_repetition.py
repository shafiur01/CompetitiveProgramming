class Solution():
    def longest_consecutive(self, nums):
        num_set = set(nums)
        longest_sequence = 0
        for n in num_set:
            # check if it's the start of a sequence
            if n-1 not in num_set:
                length = 0
                while n+length in num_set:
                    length += 1
                longest_sequence = max(length, longest_sequence)
        return longest_sequence


if __name__ == "__main__":
    sol = Solution()
    list1 = [-6,4,4,-3,-8,-1]
    print(sol.longest_consecutive(list1))