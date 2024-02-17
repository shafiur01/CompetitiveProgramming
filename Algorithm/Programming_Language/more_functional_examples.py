from functools import reduce


# This is a simple add function. It will add the two datapoints together
# Used in Problem 1
def add(a, b):
    return a + b


# This is a simple greater than function. It returns a > b
# Used in Problem 1
def greater_than(a, b):
    return a > b


# A simple multiplication function
# Used in Problem 1
def mul(a, b):
    return a * b


# PROBLEM 1
# This function first checks to see if two arrays are the same length.
# If so, it will run a map between the two arrays with the input function my_func
def array_func(my_func, array1, array2):
    if (len(array1) != len(array2)):
        return "Arrays are not the same length"
    return list(map(my_func, array1, array2))


# PROBLEM 2
# This function will take in a multilevel array.
# It will generate the average of each entered array, and then return the maximal value
# of the averages
def reduce_avg(array):
    # The outer reduce takes as input a mapped reduction of the entire input array
    # That mapped reduction is the following command:
    # map(lambda z: reduce(lambda a,b: a + b, z)/len(z), array)
    # This map will iterate through array, which is an array of arrays.
    # The reduce call will add every item from array member z (which will be an integer array)
    # We will then divide the reduction (a single number) by the overall length of z
    return reduce(lambda x, y: x if x > y else y, list(map(lambda z: reduce(lambda a, b: a + b, z) / len(z), array)))


# PROBLEM 3
# This is the first of the filtering functions. It does not return data in order.
# It filters into three sublists: even numbers not evenly divisible by 3, even numbers divisible by 3, and odd numbers.
# It squares the first filter, cubes the second, and generates 1/x for the third
def filter_func(array):
    evens1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0 and x % 3 != 0, array)))
    evens2 = list(map(lambda x: x ** 3, filter(lambda x: x % 2 == 0 and x % 3 == 0, array)))
    odds = list(map(lambda x: 1 / x, filter(lambda x: x % 2 == 1, array)))
    # x ** 2 if x % 2 == 0 and x % 3 != 0 else x ** 3 if x % 2 == 0 and x % 3 == 0 else 1/x
    return evens1 + evens2 + odds


# Helper function. Runs the above filter operation for a given number
def filter_helper(a):
    if (a % 2 == 0 and a % 3 != 0):
        return a ** 2
    elif (a % 2 == 0 and a % 3 == 0):
        return a ** 3
    else:
        return 1 / a


# PROBLEM 3 Extra Credit
# This function utilizes the above helper function to return a value based on the input number
def better_filter(array):
    return list(map(filter_helper, array))


# PROBLEM 4
# This function will take in two arrays and an input function.
# It will apply the function to every pairing (i,j) for each array
# It will create a 2-dimensional array containing the results.
def generate_2d(my_func, array1, array2):
    # The outer map takes as input just array1, and passes each item from array1 into a map call
    # The inner map takes as input array2 (note it does not take a as input, rather it uses a as a constant
    # The inner map applies the input function my_func to a from array1, and each item b form array2
    return list(map(lambda a: list(map(lambda b: my_func(a, b), array2)), array1))


def main():
    print("The first test will be to craft a method which will take a function as input func1, and two arrays")
    print("The arrays must be the same size")
    print("The function will return an array containing the results of func1(arr1[i], arr2[i])")
    print("It must use the map function, it cannot use a for loop")
    array1 = [1, 2, 3, 4, 5]
    array2 = [6, 7, 8, 9, 10]
    array3 = array_func(add, array1, array2)
    print(array3)
    print(
        "The next function will create a new list based on the input. If a number X is odd, the new list will contain the inverse (1/X). If a number X is even, the new list will contain the number squared or cubed, depending on divisibility by three.")
    array4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    array5 = filter_func(array4)
    print(array5)

    print(
        "\nThe above function call contains all members of the original integer array, however it places them out of order. We would have to use a for loop to place them correctly. Can we get there without the loop?")
    array6 = better_filter(array4)
    print(array6)
    # array8 = generate_2d(exp, rand1, rand2)


    print("We will now generate a 2-D array composed of every item from array 1 multiplied with every item from array6")
    print("That will then be used as input to find the greatest average from that input")
    array7 = generate_2d(mul, array1, array6)
    max_val = reduce_avg(array7)
    print("Every sub array from array7")
    # This call allows print to iterate through every item of the array with a specified separator between them
    print(*array7, sep="\n")
    print("The maximal value of the averages from array7 is: %f" % max_val)


main()

