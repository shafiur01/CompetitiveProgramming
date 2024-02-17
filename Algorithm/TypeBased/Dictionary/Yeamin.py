# # x = {'AA': 3, 'BB': 2, 'CC': 1, 'DD': 0}
#
# my_dict = {'Cow': 3, 'Goat': 2, 'Cat': 1, 'Horse': 0}
#
#
# for k, v in my_dict.items():
#     print(v, k)
#
# m = {v: k for k, v in my_dict.items()}[0]
# print(m)

# for k in my_dict.keys():
#     print(my_dict[k])


# ab = [1, 2, 3, 4]
# n = [i*2 for i in ab]
# print(n)


# y = []
# for i in range(len(ab)):
#     y.append(ab[i]*2)
# print(y)

# ab = [1, 2, 3, 4]
# for i in ab:
#     y.append(i*2)
# print(y)



# v1 = list(my_dict.keys()) [list(my_dict.values()).index(1)]

# print(list(my_dict.keys()))
# print(my_dict.pop('Cow'))
# print(my_dict.keys())

# x = list(my_dict.keys())
# print(x)
#
#
# y = list(my_dict.values())
# print(y)
#
#
# z = x[2]
# print(z)

# print(y.index(1))

# v2 = {v:k for k, v in my_dict.items()}[0]
# # print(v1, v2)
#
#
# print(my_dict['AA'])


x = [1, 2, 9, 3, 30]

# traverse through the array
# check if any index element between 1-4 == 9
# if it's 9 -> return True,
# else return False


# for i in range(len(x)):
#     if x[i] == 9:
#         print(True)
#         break
#     else:
#         continue
# aaabbbbaaaa
# 1, 2, 3


# y = [5, 4, 6, 3, 1, 2, 3]
# z = []
# for i in range(len(y)-1, -1, -1):
#     z.append(y[i])
# print(z)
#
# if len(y) < 3:
#     print(False)
# else:
#     for i in range(len(y)):
#         if y[i] == 1:
#             if y[i:i+4] == [1, 2, 3]:
#                 print(True)
#                 break
#             else:
#                 continue
#


# a = 'xxcaazz'
# b = 'xxbaaz'
# count = 0
#
# for i in range(len(b)):
#     if b[i:3] == a[i:3]:
#         count += 1
#     else:
#         continue
#
# print(count)

d1 = {"a": 11, "b": 12, "c": 2, "e": 3}
d2 = {"a": 3, "b": 3, "d": 25, "f": 1}

d3 = {}

for key, value in d1.items():
    if key in d2.keys():
        d3[key] = d1[key] + d2[key]
    else:
        d3[key] = d1[key]

for key, value in d2.items():
    if key not in d3.keys():
        d3[key] = d2[key]

print(d3)