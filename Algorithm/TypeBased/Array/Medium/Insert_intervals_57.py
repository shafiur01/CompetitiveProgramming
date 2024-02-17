class Solution:
    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            return [newInterval]

        i = 0
        # intervals: [1,5], [6,8]  -> [1,7], [6,8]
        # newInterval: [2,7]
        while i < len(intervals):
            if newInterval[0] <= intervals[i][1]:
                if intervals[i][0] <= newInterval[0]:
                    if intervals[i][1] >= newInterval[1]:
                        return intervals
                    else:
                        intervals[i] = [intervals[i][0], newInterval[1]]
                        break
                elif newInterval[0] <= intervals[i][0]:
                    if newInterval[1] >= intervals[i][1]:
                        intervals[i] = newInterval
                        break
                    else:
                        intervals[i] = [newInterval[0], intervals[i][1]]
                        break
            else:
                i += 1
                if i == len(intervals):
                    intervals.append(newInterval)

        # [1, 7], [6, 8]
        x = 1
        while x < len(intervals):
            if intervals[x][0] <= intervals[x-1][1]:
                if intervals[x][1] >= intervals[x-1][1]:
                    intervals[x-1] = [intervals[x-1][0], intervals[x][1]]
                    del(intervals[x])
                else:
                    del(intervals[x])
            else:
                x += 1
        return intervals


if __name__ == "__main__":
    x = Solution()
    list2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [0, 3]
    print(x.insert(list2, newInterval))

# maxArea = -1
# left, right = 0, len(height) - 1
# while left < right:
#     area = min(height[left], height[right]) * (right - left)
#     maxArea = max(maxArea, area)
#     if height[left] <= height[right]:
#         left += 1
#     else:
#         right -= 1
# return maxArea