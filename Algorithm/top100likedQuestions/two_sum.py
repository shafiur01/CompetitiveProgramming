# list = ['apple', 'mango', 'cherry']
list1 = [1,2,3,4]
target = 5

map1 = {}

for index, element in enumerate(list1):
    diff = target-element
    if diff in map1.keys():
        print([map1[diff], index])
        break
    map1[element] = index
