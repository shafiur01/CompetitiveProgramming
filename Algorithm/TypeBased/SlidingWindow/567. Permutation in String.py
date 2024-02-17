from collections import Counter


# ab
# eidbaooo
def checkInclusion(s1: str, s2: str):
    counterS1 = Counter(s1)  # (['a' = 1, 'b' = 1])
    counterS2 = Counter()
    left = 0

    for i in range(len(s2)):
        # if the difference between the index and the left is greater than the
        if i-left < sum(counterS1.values()):
            counterS2[s2[i]] += 1

        elif counterS2[s2[left]] >= 1:
            if counterS2[s2[left]] > 1:
                counterS2[s2[left]] -= 1
            else:
                del counterS2[s2[left]]
            counterS2[s2[i]] += 1
            left += 1

        if counterS1 == counterS2:
            return True

    return False


print(checkInclusion("abcdxabcde", "abcdeabcdx"))