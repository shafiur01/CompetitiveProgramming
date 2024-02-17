def countGoodSubstrings(s: str):
    # aababcabc
    left = 0
    temp_set = set()
    length = 0

    for index in range(len(s)):
        while s[index] in temp_set:
            temp_set.remove(s[left])
            left += 1

        temp_set.add(s[index])
        if len(temp_set) == 3:
            length += 1
            temp_set.remove(s[left])
            left += 1
    return length


print(countGoodSubstrings("xyzzaz"))