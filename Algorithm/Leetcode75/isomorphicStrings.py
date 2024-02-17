class Solution(object):
    def __init__(self, name):
        self.name = name

    def isIsomorphic(self, s, t):
        # s = "paper", t = "title"
        is_Isomorphic = False
        matching_dictionary = dict()

        # {'p': 't', 'a':'i', 'p':'k', 'e':'l', 'r':'e'}
        for i in range(len(s)):
            if s[i] not in matching_dictionary:
                if t[i] in matching_dictionary.values():
                    is_Isomorphic = False
                    break
                else:
                    matching_dictionary[s[i]] = t[i]
                    if (i==len(s)-1):
                        return True

            elif (matching_dictionary[s[i]] != t[i]):
                is_Isomorphic = False
                break
            else:
                is_Isomorphic = True

        return is_Isomorphic


if __name__ == "__main__":
    name = "shafiur"
    isomorphic = Solution(name)
    s = "a"
    t = "a"
    print(isomorphic.isIsomorphic(s, t))
