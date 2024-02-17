# Write a Python program that takes in two lists of integers, list1 and list2, and returns a new list that contains the
# elements that are common to both lists, in the order that they appear in list1.
# The list1 and list2 contain user entered data.
# For example
# if list1 is [1, 2, 3, 4, 5] and   list2 is [3, 1, 4, 6, 7]
# the program should print [1, 3, 4]
# Solution steps:
# 1. get integer numbers from the user and form list1 and list2
# 2. check if each item in list1 is also in list2, and if it is, add that number to the new list.
# 3. print the new list


input_string = input('please enter a few numbers here seperated by space:')
user_list = input_string.split()


input_string2 = input('please enter another few numbers here seperated by space:')
user_list2 = input_string2.split()

common_list = []
for digit in user_list:
    if digit in user_list2:
        common_list.append(digit)
print(common_list)

