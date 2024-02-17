class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i-1][1]:
                if intervals[i][1] >= intervals[i-1][1]:
                    intervals[i-1] = [intervals[i-1][0], intervals[i][1]]
                    del(intervals[i])
                else:
                    del(intervals[i])
            else:
                i += 1
        return intervals


# [[1, 3], [2, 6], [7, 10], [8, 8], [15, 18]]
if __name__ == "__main__":
    x = Solution()
    list2 = [[1,3],[7,10],[15,18],[2,6], [8,8]]
    print(x.merge(list2))
