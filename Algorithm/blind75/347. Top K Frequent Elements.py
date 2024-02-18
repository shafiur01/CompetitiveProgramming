"""Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 """


def topKFrequent(nums, k: int):
    dict1 = dict()
    # {1: 3, 2: 2, 3: 1}

    for number in nums:
        if number not in dict1:
            dict1[number] = 1
        else:
            dict1[number] += 1

    # Step 1: Sort the keys of the dictionary based on their values in descending order
    sorted_keys = sorted(dict1, key=dict1.get, reverse=True)

    # Step 2: Slice the sorted list to get the first k elements
    top_k_elements = sorted_keys[:k]
    return top_k_elements

print(topKFrequent([2,2,3,1,1,1], 2))
