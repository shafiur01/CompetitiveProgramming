"""
Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.
The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.

A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Example 1:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: true
Example 2:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
Output: false
Example 3:

Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
Output: true
"""

import math


class Solution:
    def validSquare(self, p1, p2, p3, p4) -> bool:
        list1 = [p1, p2, p3, p4]
        list2 = []
        for i in range(len(list1)):
            for j in range(i+1, len(list1)):
                list2.append(self.distance(list1[i], list1[j]))
        list2.sort()
        if len(set(list2)) == 2 and list2[0] == list2[1] == list2[2] == list2[3] and list2[4] == list2[5]:
            return True
        else:
            return False

    def distance(self, c1, c2):
        d = math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)
        return d


if __name__ == "__main__":
    s = Solution()
    p1 = [0, 0]
    p2 = [1, 1]
    p3 = [1, 0]
    p4 = [0, 1]
    print(s.validSquare(p1, p2, p3, p4))
