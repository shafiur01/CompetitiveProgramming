class removingDuplicateSolution:
    def __init__(self, name):
        self.name = name

    def removingDuplicate(self, list):
        pointer = 0
        checking_element = list[pointer]
        for i in range(len(list)):
            if i == 0:
                continue
            elif list[i] == checking_element:
                continue
            else:
                pointer += 1
                list[pointer] = list[i]
                checking_element = list[pointer]

        return pointer+1



if __name__ == "__main__":
    name = "Shafiur"
    operator = removingDuplicateSolution(name)
    list1 = [0,0,1,1,1,2,2,3,3,4,5,6,7,7,8]

    print(operator.removingDuplicate(list1))




