import math
import os
import random
import re
import sys
from collections import Counter


def matchingStrings(stringList, queries):
    # Write your code here
    # this will count the total unique string in the array, we can also build a dictionary for keeping the count
    StringCount = Counter(stringList)
    print(StringCount)

    array1 = [0] * len(queries)

    # going over the queries and checking if the element is in the stringlist first, if it is then we check its count from the StringCount and store it in the array1
    for i in range(len(queries)):
        if queries[i] in stringList:
            array1[i] = StringCount[queries[i]]
        else:
            array1[i] = 0
    return array1


print(matchingStrings(['ab', 'ab', 'abc'], ['ab', 'abc', 'bc']))
