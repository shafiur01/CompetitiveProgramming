# list1 = [2,1,2,0,1]
#
# if len(list1) == 1:
#     print(0)
# else:
#     lowest = list1[0]
#     highest = list1[1]
#     profit = 0
#     for index in range(1, len(list1)):
#         if list1[index] > highest:
#             highest = list1[index]
#         if list1[index] < lowest:
#             lowest = list1[index]
#             highest = 0
#             continue
#         if highest - lowest > profit:
#             profit = highest - lowest
#     print(profit)
prices = [7,1,5,3,6,4]


proffit = 0
highest = prices[0]
lowest = prices[0]

for price in prices:
    if price > highest:
        highest = price
        proffit = max(proffit, highest - lowest)
    elif price < lowest:
        highest = price
        lowest = price
print(proffit)

