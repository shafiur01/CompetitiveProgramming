"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""


class Solution:
    def characterReplacement(self, s: str, k: int):
        n = 0
        count = 0
        max_length = 0
        temp_index = -1
        x = k
        tmp_str = ""
        # AABBBBA
        # at first we travel through the string and look
        while n <= len(s):
            # for the first element we skip since there is no other element beofre it
            if n == 0:
                count = 1
                tmp_str += s[0]
                max_length = 1
            else:
                # if a letter is same as it's previous element then we increase the count and go forward
                # if not then we decrease the k by one everytime we encounter a new letter, but there is a very important thing the first time
                # we encounter a new letter then we have to remember its index number = temp_index, so that we can start from that element in
                # the next cycle putting n = temp_index
                if s[n] == temp_index[n - 1]:
                    count += 1
                    tmp_str += s[n]
                    max_length = max(max_length, count)
                else:
                    if x >= 1:
                        if x == k:
                            temp_index = n
                        x -= 1
                        count += 1
                        tmp_str += s[temp_index-1]
                        max_length = max(max_length, count)
                    else:
                        n = temp_index
                        count = 0
                        x = k
            n += 1
        return max_length


if __name__ == "__main__":
    x = Solution()
    string = 'AABABBA'
    print(x.characterReplacement(string, 1))