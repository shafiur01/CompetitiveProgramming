class Solution:
    def maxSubArray(self, List):
        # [-1, 1, 0, -3, 3, 2, -4, 2, 6, -3, 4, 8, 8, -4]
        maxSubArraySum = List[0]
        currentSum = 0

        for i in List:
            if currentSum < 0:
                currentSum = 0
            currentSum += i
            maxSubArraySum = max(maxSubArraySum, currentSum)
            
        return maxSubArraySum

if __name__ == "__main__":
    maximumSubArray = Solution()
    array = [-1, 1, 0, -3, 3, 2, -4, 2, 6, -3, 4, 8, 8, -4]
    print(maximumSubArray.maxSubArray(array))

