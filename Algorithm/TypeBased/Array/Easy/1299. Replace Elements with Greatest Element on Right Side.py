"""Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.



Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation:
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.
Example 2:

Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.


Constraints:

1 <= arr.length <= 104
1 <= arr[i] <= 105
"""


def replaceElements(arr):
    max_seen = -1               # Initialize the maximum seen so far to -1 (since -1 is the value for the last element)
    for i in range(len(arr) - 1, -1, -1):   # Traverse the array from right to left
        temp = arr[i]                       # Temporarily store the current element
        arr[i] = max_seen                   # Replace the current element with the maximum seen so far
        max_seen = max(max_seen, temp)      # Update the maximum seen so far
    return arr

    # return x


print(replaceElements([17,18,5,4,6,1]))