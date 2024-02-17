"""
692. Top K Frequent Words
Given an array of strings words and an integer k, return the k most frequent strings.
Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

Constraints:

1 <= words.length <= 500
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]

Follow-up: Could you solve it in O(n
"""

from collections import Counter
class Solution:
    def topKFrequent(self, words, k: int): # -> List[str]:
        # counter_object = Counter(setence)
        # reversed_dict = dict(sorted(counter_object.items(), key=lambda item: (-item[1])))
        # print(reversed_dict)
        # sorted_words = [word for word, count in sorted(reversed_dict.items(), key=lambda item: (-item[1], item[0]))][:k]
        # return sorted_words
        map = dict()
        for word in words:
            if word not in map:
                map[word] = 1
            else:
                x = map[word]
                x += 1
                map[word] = x

        reversed_dict = dict(sorted(map.items(), key=lambda item:item[1], reverse=True))
        list1 = [key for key, value in sorted(reversed_dict.items(), key=lambda item: (-item[1], item[0]))][:2]

        return list1



if __name__ == "__main__":
    x = Solution()
    words = ["the", "is","day","is","sunny","the","sunny","the","sunny","is","is"]
    print(x.topKFrequent(words, 2))