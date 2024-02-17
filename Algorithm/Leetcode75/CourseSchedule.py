class Solution:
    def __init__(self, name):
        self.name = name

    # constrains
    # 1 <= numCourses <= 2000
    # 0 <= prerequisites.length <= 5000
    # prerequisites[i].length == 2
    # 0 <= ai, bi < numCourses
    # All the pairs prerequisites[i] are unique.
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        isTrue = False
        if len(prerequisites) < 1:
            isTrue = True
            return isTrue
        for i in range(len(prerequisites)):
            if numCourses == 1:
                isTrue = True
                break
            if (prerequisites[i][0] < prerequisites[i][1]):
                isTrue = False
            else:
                isTrue = True
        return isTrue


if __name__ == "__main__":
    name = 'Shafiur Rahman'
    number = 1
    pre = []
    isTru = Solution(name)
    print(isTru.canFinish(number, pre))

