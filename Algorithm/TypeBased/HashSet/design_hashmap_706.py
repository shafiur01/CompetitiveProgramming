class MyHashMap:

    def __init__(self):
        self.dict1 = dict()

    def put(self, key: int, value: int) -> None:
        if key in self.dict1.keys():
            self.dict1[key] = value
        else:
            self.dict1[key] = value

    def get(self, key: int) -> int:
        if key in self.dict1.keys():
            return self.dict1[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.dict1.keys():
            del self.dict1[key]


if __name__ == "__main__":
    myHashMap = MyHashMap()
    myHashMap.put(1, 1)  #; // The
    # map is now[[1, 1]]
    myHashMap.put(2, 2)  #; // The
    # map is now[[1, 1], [2, 2]]
    print(myHashMap.get(1))  #; // return 1, The
    # map is now[[1, 1], [2, 2]]
    print(myHashMap.get(3)) #; // return -1(i.e., not found), The
    # map is now[[1, 1], [2, 2]]
    myHashMap.put(2, 1)  #; // The
    # map is now[[1, 1], [2, 1]](i.e., updat the existing value)
    print(myHashMap.get(2))  #; // return 1, The
    # map is now[[1, 1], [2, 1]]
    myHashMap.remove(2)  #; // remove the mapping
    # for 2, The map is now[[1, 1]]
    print(myHashMap.dict1)
    print("Hi: " , myHashMap.get(2))  #; // return -1(i.e., not found), The
    # map is now[[1, 1]]