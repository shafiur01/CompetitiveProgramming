list = [2,3,4,1,1]

# set1 = set(list)
# print(len(list)!=len(set1))

set1 = set()
for element in list:
    if element in set1:
        print(True)
        break
    else:
        set1.add(element)
print(False)