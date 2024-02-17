"""You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.
You are also given an integer k, which is the desired number of consecutive black blocks.
In one operation, you can recolor a white block such that it becomes a black block.
Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.
Example 1:

Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW".
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.
Example 2:

Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.
"""

# This function was coded in white board and got it right in the second time. Good Advancement in the learning process
def minimumRecolors(blocks: str, k: int):
        left = 0
        right = left + k
        B_count = 0
        min_swap_for_k_consecutive_B = k

        # WBBWWBBWBW
        while right <= len(blocks):
                x = [9, 4, 1, 7, 14, 17, 17, 16].sort()
                B_count = blocks[left:right].count("B")
                swap_in_this_particular_string = k - B_count
                min_swap_for_k_consecutive_B = min(swap_in_this_particular_string, min_swap_for_k_consecutive_B)
                left += 1
                right += 1
        return min_swap_for_k_consecutive_B



print(minimumRecolors("BWBB", 2))