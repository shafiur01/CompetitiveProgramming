class Solution:
    def sortByBits(self, list):  # List[int]:
        # # way 1
        # list.sort()
        # # map = dict()
        # list2 = []
        # for element in list:
        #     count = 0
        #     binaryNumber = str(bin(element))
        #     for digit in binaryNumber[2:]:
        #         if digit == str(1):
        #             count += 1
        #
        #     list2.append([[count],[element]])
        #     list2.sort()
        # list3 = []
        # for i in list2:
        #     list3.extend(i[1])
        # print(list3)

        return sorted(list, key=lambda digit: (bin(digit).count("1"), digit))


if __name__ == "__main__":
    binarySearch = Solution()
    # notice the array is sorted
    list1 = [10, 100, 1000, 10000]
    print(binarySearch.sortByBits(list1))
