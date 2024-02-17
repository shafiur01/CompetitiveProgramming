def characterReplacement(s: str, k: int):
    # We made a dictionary
    count = {}
    left = 0
    current_max = 0

    # AABABBA
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)

        while (r-left+1) - max(count.values()) > k:
            count[s[left]] -= 1
            left += 1
        current_max = max(current_max, r-left+1)
    return current_max


print(characterReplacement("AABABBACAAA", 3))