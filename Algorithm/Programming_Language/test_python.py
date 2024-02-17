# Shafiur Rahman Bhauyan

# Create a function that takes as input an array of comparable datapoints
# It will use functional programming to generate the sorted array
# def func_one(my_data):


# Main program with Extra Credit
# Insertion sort method is an inplace algorithm to sort an array
from functools import reduce
import random


# Helper function to insert an element into a list
def insert_into_sorted(sorted_list, element):
    for i, current in enumerate(sorted_list):
        if element <= current:
            return sorted_list[:i] + [element] + sorted_list[i:]
    return sorted_list + [element]


# Sorting function using lambda and reduce
def func_one(my_data):
    return reduce(lambda acc, val: insert_into_sorted(acc, val), my_data, [])


# This function will take as input two arrays of integers.
# It will first create a matrix by multiplying every value of each array together
# It will then iterate through the matrix, taking count of the occurrences of each product
# Once we have accounted for all products, we will then return the set of values that
# only appear in the array once


def func_two(array_one, array_two):
    # Creating the product matrix
    product_matrix = map(lambda x: map(lambda y: x * y, array_two), array_one)

    # Flattening the matrix into a single list
    flattened_matrix = reduce(lambda x, y: x + list(y), product_matrix, [])

    # Counting the occurrences
    count_dict = reduce(lambda acc, val: {**acc, val: acc.get(val, 0) + 1}, flattened_matrix, {})

    # Filtering to find unique products
    unique_products = set(filter(lambda x: count_dict[x] == 1, count_dict))

    return unique_products


def main():
    test = []
    for i in range(50):
        test.append(random.randint(0, 100))

    print(test)
    print("When the above array is sorted, the array becomes: %s" % (func_one(test)))

    array_one = []
    array_two = []
    for i in range(10):
        array_one.append(random.randint(1, 10))
        array_two.append(random.randint(1, 10))

    print("The two arrays we will test func_two with:\n%s\n%s" % (array_one, array_two))
    print(func_two(array_one, array_two))


main()

