def containsNearbyDuplicate(nums, k: int):
    i = 0
    while i < len(nums):
        digit = nums[i]
        if digit in nums[i + 1:]:
            index2 = (i+1) + nums[i + 1:].index(digit)
            if abs(i - index2) <= k:
                return True
            else:
                i += 1
                continue
        else:
            i += 1
            continue
    return False


print(containsNearbyDuplicate([1,2,3,1,2,3], 2))