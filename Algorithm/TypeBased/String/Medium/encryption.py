import math
import os
import random
import re
import sys


# Complete the 'encryption' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.


def encryption(s):
    y = ""
    for i in range(len(s)):
        if s[i] == " ":
            y += ""
        else:
            y += s[i]
    high = math.ceil(math.sqrt(len(y)))

    dict1 = {}
    index = 0
    while index < len(y):
        for j in range(high):
            if index >= len(y):
                break
            if j not in dict1:
                dict1[j] = str(y[index])
                index += 1
            else:
                dict1[j] += y[index]
                index += 1

    return_string = ""
    for i in range(high):
        return_string += dict1[i] + " "

    return return_string


string1 = "if man was meant to stay on the ground god would have given us rooots"
print(encryption(string1))