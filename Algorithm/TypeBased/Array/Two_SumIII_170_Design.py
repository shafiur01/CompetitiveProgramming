"""
Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.
Implement the TwoSum class:

TwoSum() Initializes the TwoSum object, with an empty array initially.
void add(int number) Adds number to the data structure.
boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.

Example 1:
Input
["TwoSum", "add", "add", "add", "find", "find"]
[[], [1], [3], [5], [4], [7]]
Output
[null, null, null, null, true, false]

Explanation
TwoSum twoSum = new TwoSum();
twoSum.add(1);   // [] --> [1]
twoSum.add(3);   // [1] --> [1,3]
twoSum.add(5);   // [1,3] --> [1,3,5]
twoSum.find(4);  // 1 + 3 = 4, return true
twoSum.find(7);  // No two integers sum up to 7, return false
"""


class TwoSum:

    def __init__(self):
        self.List = []

    def add(self, number: int): # -> None:
        self.List.append(number)

    def find(self, value: int): # -> bool:
        self.List.sort()
        left, right = 0, len(self.List)-1
        while left < right:
            summation = self.List[left] + self.List[right]
            if summation == value:
                return True
            elif summation < value:
                left += 1
            elif summation > value:
                right -= 1
        return False


# Your TwoSum object will be instantiated and called as such:
if __name__ == "__main__":
    twoSum = TwoSum()
    twoSum.add(1) #; // [] --> [1]
    twoSum.add(3) #; // [1] --> [1, 3]
    twoSum.add(5) #; // [1, 3] --> [1, 3, 5]
    print(twoSum.find(4)) #; // 1 + 3 = 4,
    print(twoSum.find(7)) #; // No two integers sum up to 7, return false