# from functools import reduce
#
# array1 = [[2, 2, 2, 5, 3, 7, 5], [6, 4, 4, 4, 6, 4, 6, 9], [8, 12, 12, 8, 20]]
#
# array2 = [1, 1, 1, 5, 2, 2, 2, 5, 3, 7, 7, 7]
#
#
# def make_Dict(dict, item):
#     if item not in dict.keys():
#         dict[item] = 1
#     else:
#         dict[item] += 1
#     return dict
#
#
# def remove_Max_Occurance(dict1):
#     # Your dictionary with digits as keys and counts as values
#
#     # Use reduce to find the maximum occurrence
#     max_digit = reduce(lambda x, y: x if x[1] > y[1] else y, dict1.items())
#
#     # Now creating a new dictionary without the max occurrence digit
#     digit_counts = {digit: count for digit, count in dict1.items() if digit != max_digit[0]}
#
#     # print("Digit with maximum occurrence:", max_digit[0])
#     # print("New dictionary without the max occurrence digit:", digit_counts)
#     return max_digit[0], digit_counts
#
#
# # Lambda function to call remove_Max_Occurance twice and store the results
# find_two_max_digits = lambda dict1: [remove_Max_Occurance(dict1)[0]] + [remove_Max_Occurance(remove_Max_Occurance(dict1)[1])[0]]
#
# # Calling the lambda function and store the two maximum digits
# # print("Two digits with maximum occurrences:", find_two_max_digits(digit_counts))
#
#
# def find_Max2_Occurance(array2):
#     dict1 = dict()
#     arr3 = list(map(lambda element: make_Dict(dict1, element), array2))
#     print(dict1)
#     list1 = find_two_max_digits(dict1)
#     print(list1)
#
#
# print(find_Max2_Occurance(array2))
#
#







# from functools import reduce
#
# # Your dictionary with digits as keys and counts as values
# digit_counts = {0: 20, 1: 4, 2: 20, 3: 3, 4: 7, 5: 17, 6: 5, 7: 8, 8: 13, 9: 20}
#
#
# # Function to keep the top two counts
# def keep_top_two(acc, item):
#     (first, second) = acc
#     if item[1] > first[1]:
#         return (item, first)
#     elif item[1] > second[1]:
#         return (first, item)
#     return acc
#
#
# # Initialize the accumulator with two tuples with the smallest possible counts
# initial = (('first', 0), ('second', 0))
#
# # Run the reduction
# result = reduce(keep_top_two, digit_counts.items(), initial)
#
# # The result now contains the top two
# top_two_digits = [result[0][0], result[1][0]]
#
# print(top_two_digits)  # This will print the keys with the top two counts
#
#
#







from functools import reduce

# # Your dictionary with digits as keys and counts as values
# digit_counts = {0: 10, 1: 4, 2: 20, 3: 3, 4: 7, 5: 17, 6: 5, 7: 8, 8: 13, 9: 11}
# print(digit_counts)
#
#
# # Reduce function to find the key with the maximum value
# def find_max_key(acc, item):
#     return item if item[1] > acc[1] else acc
#
#
# # Use reduce to find the maximum occurrence
# max_key, max_value = reduce(find_max_key, digit_counts.items())
#
#
# # Now remove the max_key from the dictionary
# new_digit_counts = {key: value for key, value in digit_counts.items() if key != max_key}
#
# print(max_key)  # This will print the key with the maximum count
# print(new_digit_counts)  # This will print the new dictionary without the max_key











from functools import reduce
def remove_Max_Occurance(dict1):
    # Your dictionary with digits as keys and counts as values

    # Use reduce to find the maximum occurrence
    max_digit = reduce(lambda x, y: x if x[1] > y[1] else y, dict1.items())

    # Now creating a new dictionary without the max occurrence digit
    digit_counts = {digit: count for digit, count in dict1.items() if digit != max_digit[0]}

    # print("Digit with maximum occurrence:", max_digit[0])
    # print("New dictionary without the max occurrence digit:", digit_counts)
    return max_digit[0], digit_counts


digit_counts = {0: 10, 1: 4, 2: 20, 9: 30}

print(remove_Max_Occurance(digit_counts)[0])
print(remove_Max_Occurance(digit_counts)[1])
