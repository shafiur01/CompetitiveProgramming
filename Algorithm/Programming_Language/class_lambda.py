from functools import reduce


# this is the nested for loop down into one line, it's adding each subarray and printing them
data2 = [[1, 2, 3], [4, 5, 6, 7], [8, 9], [10, 11, 12, 12, 12, 12]]
new_data = list(map(lambda x: reduce(lambda a, b: a+b, x), data2))
print(new_data)



# def lamdaFunc(a, b):
#     mul5 = lambda a,b : a[b] * 5
#     data = [1,2,3,4,5,6]
#     print(mul5, 3)
#
#
#     return (lambda a, b: a + b)(a, b)
#
#
# print(lamdaFunc(4,3))
# # Map is a default data in the python, when the shortest array is finished then the count in finished too


# data1 = [0, 1, 2, 4, 4, 5]
# print(data1)
# # list(map(lambda x: print(x**2), data))
#
#
# def my_func(data, index):
#     data[index] += 5
#
# x = list(map(lambda x: my_func(data1, 5), data1))
#
