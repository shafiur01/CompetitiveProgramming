nums = [1,2,3,4]
currentSum = 0
for i in range(1, len(nums)):
    nums[i] = nums[i - 1] + nums[i]
print(nums)
