class Solution:
    def trap(self, List):
        left, right = 0, len(List)-1
        left_max, right_max = List[left], List[right]
        count = 0

        while left < right:
            if min(left_max,  right_max) == left_max or left_max == right_max:
                if left_max - List[left] > 0:
                    count += left_max-List[left]
                    left += 1
                    left_max = max(left_max, List[left])
                else:
                    left += 1
                    left_max = max(left_max, List[left])
            else:
                if right_max - List[right] > 0:
                    count += right_max - List[right]
                    right -= 1
                    right_max = max(right_max, List[right])
                else:
                    right -= 1
                    right_max = max(right_max, List[right])
        return count


if __name__ == "__main__":
    x = Solution()
    list1 = [4,2,0,3,2,5]
    print(x.trap(list1))




