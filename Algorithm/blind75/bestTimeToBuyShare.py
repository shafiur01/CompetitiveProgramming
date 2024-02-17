import random


class Solution(object):
    def __init__(self, name):
        self.name = name

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """


        probableBuyingDay = 0
        probableSellingDay = 1
        maximumProfit = 0

        while probableSellingDay < len(prices):
            if prices[probableBuyingDay] < prices[probableSellingDay]:
                profit = prices[probableSellingDay] - prices[probableBuyingDay]
                maximumProfit = max(profit, maximumProfit)
            else:
                probableBuyingDay = probableSellingDay
            probableSellingDay += 1

        return maximumProfit




if __name__ == "__main__":
    name = "Shafiur"
    BestTimeTobuyShare = Solution(name)
    array = [2, 10, 3, 36, 1, 20, 16, 37]
    # array = [3, 10, 4, 30, 1, 20, 16, 29]
    # for i in range(9):
    #     array.append(random.randint(0, 20))
    # print(array)
    print(BestTimeTobuyShare.maxProfit(array))
