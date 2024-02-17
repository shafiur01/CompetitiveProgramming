class validParenthesesSolution:
    def __init__(self, name):
        self.name = name

    def validParentheses(self, parentheses):
        dictionary1 = {"(": ")", "{": "}", "[": "]"}

        # this line converts the string of parentheses into a list of parentheses
        parentheses1 = []
        
        # # ()({[]()})
        # for i in range(len(parentheses)):
        #     if parentheses[i] in dictionary1.keys():
        #         parentheses1.append(parentheses[i])
        #         if i == len(parentheses) - 1 and len(parentheses1) != 0:
        #             return False
        #         continue
        #     elif parentheses[i] in dictionary1.values():
        #         if (len(parentheses1)==0):
        #             return False
        #         index = len(parentheses1) - 1
        #         if dictionary1[parentheses1[index]] == parentheses[i]:
        #             parentheses1.pop(index)
        #             if i == len(parentheses)-1 and len(parentheses1) != 0:
        #                 return False
        #             continue
        #         else:
        #             return False
        #
        # return True
        my_stack = []

        for i in parentheses:
            if i in '({[':
                my_stack.append(i)
            elif i in ')}]':
                if len(my_stack) == 0 or i != dictionary1[my_stack.pop()]:
                    return False

        return len(my_stack) == 0


if __name__ == "__main__":
    name = "Shafiur"
    operator = validParenthesesSolution(name)
    parentheses = "[(){()({})}]("

    print(operator.validParentheses(parentheses))




