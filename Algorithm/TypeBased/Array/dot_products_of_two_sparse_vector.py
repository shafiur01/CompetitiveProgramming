class SparseVector:
    def __init__(self, list):
        self.list = list

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vector):
        z = self.list*vector
        return z
        

if __name__ == "__main__":
    sol = SparseVector
    list1 = [1, 1, 0, 0 ,2, 0, 0, 0, 1]
    list2 = [1, 1, 2, 3, 3, 3, 4, 4, 4]

    v1 = SparseVector(list1)
    v2 = SparseVector(list2)
    print(v1.dotProduct(v2))


