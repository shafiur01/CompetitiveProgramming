class largestCommonStringSolution:
    def __init__(self, name):
        self.name = name

    def largestCommonString(self, list):
        size = len(list)
        list.sort()
        str = ""
        if len(list[0]) == 0:
            return str
        for i in range(len(list[0])):
            if list[0][i] == list[size-1][i]:
                str += list[0][i]
                if i == len(list[0])-1:
                    return str
            else:
                return str


if __name__ == "__main__":
    name = "Shafiur"
    operator = largestCommonStringSolution(name)
    list1 = ["a", "abc", "acb", "bad", "ab", "d" ]
    print(operator.largestCommonString(list1))




