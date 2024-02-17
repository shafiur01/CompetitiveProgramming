class Solution:
    def maxProduct(self, nums) -> int:
        # [2,3,-2,-5, 0, 4, -6, -3]
        # if we encounter a -ve digit then we've to count the number of negative elements if it's even then we add it to the previous product of array or later products, but if the count is odd then we skip the negative portion

        left, right = 0, 1
        current_max = nums[left]
        max_product = nums[left]

        while right < len(nums):
            if current_max == 0:
                if right == len(nums)-1:
                    current_max = nums[right]
                    right += 1
                    max_product = max(max_product, current_max)
                else:
                    left = right
                    right = left + 1
                    current_max = nums[right]
                    max_product = max(max_product, current_max)

            else:
                current_max *= nums[right]
                right += 1
                max_product = max(max_product, current_max)
        return max_product


if __name__ == "__main__":
    x = Solution()
    list1 = [2,3,-2,4]
    print(x.maxProduct(list1))