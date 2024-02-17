class Solution:
    def uniqueOccurrences(self, list):
        # '''Making a map which will help to keep the count of the number of occurence of each individual element
        #  in the array'''
        # map1 = {}
        # for i in list:
        #     if i not in map1:
        #         map1[i] = 1
        #     else:
        #         map1[i] += 1
        # '''A set is made from the values of the map'''
        # set1 = set(map1.values())
        # '''if there is any duplicate in the map then the len of set1 will be smaller then the map1.values()
        # so the logic below will return true if the count of all the element of the set is unique, if there is any
        # duplicate then it will return false'''
        # return len(set1) == len(map1.values())

        l = []
        for i in set(list):
            l.append(list.count(i))
        s = set(l)

        return len(s) == len(l)


if __name__ == "__main__":
    sol = Solution()
    list1 = [1,2,2,3,3,3,4,4,4]
    x = sol.uniqueOccurrences(list1)
    print(x)