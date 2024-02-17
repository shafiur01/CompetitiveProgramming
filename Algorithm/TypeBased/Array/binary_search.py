class Solution:
    def search(self, list, target):  # the output would be an int
        left = 0
        right = len(list)-1

        while left <= right:
            mid_value_index = (left+right)//2
            if list[mid_value_index] == target:
                return mid_value_index
            elif list[mid_value_index] < target:
                left = mid_value_index+1
            elif list[mid_value_index] > target:
                right = mid_value_index-1
            else:
                return -1


if __name__ == "__main__":
    binarySearch = Solution()
    # notice the array is sorted
    list1 = [-1,0,3,5,9,12]
    print(binarySearch.search(list1, 9))