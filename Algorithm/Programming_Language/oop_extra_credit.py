from functools import reduce


# extra credit Function one
def is_numeric(val):
    return isinstance(val, (int, float))


# Functions to find out the maximum product from an array
def find_highest_product(arr):
    def min_max_product(row):
        # checking if all the elements of each of the array is numeric or not. If it is numeric then it will proceed
        if not all(map(lambda row: all(map(is_numeric, row)), arr)):
            raise ValueError("Input contains non-numeric values. Please Enter a Valid Value")

        # Finding the Minimum value of each array
        min_val = reduce(lambda x, y: x if x < y else y, filter(is_numeric, row))

        # Finding the Maximum value of each array
        max_val = reduce(lambda x, y: x if x > y else y, filter(is_numeric, row))
        return min_val, max_val

    # making a 2D array with all min and max from the given 2D array
    products = list(map(min_max_product, arr))
    # print(products)

    # Using reduce function to traverse through the products array and then returning the array with maximum product
    max_product_pair = list(reduce(lambda sub_array1, sub_array2: sub_array1 if sub_array1[0]*sub_array1[1]>
sub_array2[0] * sub_array2[1] else sub_array2, products))

    return max_product_pair








# Second Function of Extra Credit
# Helper function to check if a number is prime
def is_prime2(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


# A helper function to return a recursive lambda which helps to find in prime factors
def make_recursive_lambda(f):
    return lambda n, start=2: f(f, n, start)


# The recursive lambda function that computes prime factors
prime_factors2 = make_recursive_lambda(lambda self, n, start: [] if n == 1 else
[start] + self(self, n // start, start) if n % start == 0 else
self(self, n, next(filter(lambda x: n % x == 0, range(start + 1, int(n ** 0.5) + 1)), n)))


# Function to check if the number is semiprime by counting the number of prime factors is 2 or not
def is_semiprime2(n):
    factors = prime_factors2(n)
    return len(factors) == 2 and factors[0] * factors[1] == n


# Rest of the functions remain unchanged
# Function to flatten a matrix
def flatten_matrix(matrix):
    return reduce(lambda x, y: x + y, matrix)


# Function to categorize numbers
def categorize_numbers2(matrix):
    flat_matrix = flatten_matrix(matrix)
    primes = list(filter(is_prime2, flat_matrix))
    print("The prime set: ", primes)

    semiprimes = list(filter(is_semiprime2, flat_matrix))
    print("The semi-prime set: ", semiprimes)

    other_numbers = list(filter(lambda x: x not in primes and x not in semiprimes, flat_matrix))
    print("The other number set is: ", other_numbers , "\n\n")

    return primes, semiprimes, other_numbers


# function to make dictionary of the digit and it's count
def my_dict2(dict, item):
    if item not in dict.keys():
        dict[item] = 1
    else:
        dict[item] += 1
    return dict


def remove_Max_Occurance2(dict1):
    # Using reduce to find the maximum occurrence
    max_digit = reduce(lambda x, y: x if x[1] > y[1] else y, dict1.items())

    # Now creating a new dictionary without the max occurrence digit
    digit_counts = {digit: count for digit, count in dict1.items() if digit != max_digit[0]}

    # returning the max digit and current dictionary removing the  max digit
    return max_digit[0], digit_counts


# Lambda function to call remove_Max_Occurance2 twice and store the results
find_two_max_digits = lambda dict1: [remove_Max_Occurance2(dict1)[0]] + [
    remove_Max_Occurance2(remove_Max_Occurance2(dict1)[1])[0]]


# Calling the lambda function and store the two maximum digits
def two_most_common2(array2):
    # making a dictionary to store the digit count of the passed array
    dict1 = dict()

    # filling the dict1 dictionary with the digit, and it's count by calling external function my_dict2() from inside the
    # lambda function
    arr3 = list(map(lambda element: my_dict2(dict1, element), array2))

    # making a list by calling a function which will fill the list with most frequent 2 digits from right side
    list1 = find_two_max_digits(dict1)

    # reversing the list to maintain desired sequence
    list1.reverse()

    return list1


# Main function to find the pair with the highest product among the most common
def highest_product_pair(matrix):
    # checking if all the elements of each of the array is numeric or not. If it is numeric then it will proceed
    if not all(map(lambda row: all(map(is_numeric, row)), matrix)):
        raise ValueError("Input contains non-numeric values. Please Enter a Valid Value")

    # getting the array of primes, semi-primes, others
    primes, semiprimes, others = categorize_numbers2(matrix)

    # finding the 2 most common/occurance digit from the array
    common_primes = two_most_common2(primes)
    # print("Common Prime: ", common_primes)

    common_semiprimes = two_most_common2(semiprimes)
    # print("Common semi-Prime: ", common_semi-primes)

    common_others = two_most_common2(others)
    # print("Common Other: ", common_others, "\n")

    # Making a 2D table with all the 2 most common digit from the prime, semi-prime and others list
    all_pairs = [common_primes, common_semiprimes, common_others]
    print(all_pairs)

    # Using Reduce function to find the pair with the highest product without using max or min method
    highest_product_pair = reduce(lambda x, y: x if x[0] * x[1] > y[0] * y[1] else y, all_pairs)
    print(highest_product_pair)

    # Returning only the pair with the highest product
    return highest_product_pair[:2]




# Test cases
def main():

    # Function 1
    two_dimensional_array1 = [[1, 2, 3, 4, 5], [5, 4, 3, 0], [-4, -3, 0, 3, 4]]
    two_dimensional_array2 = [[1.5, 2.5, 3.5], [4.5, 5.5, 6.5], [7.5, 8.5, 9.5]]
    two_dimensional_array3 = [[-4, -2, -4, -3, -11], [5, 10, 1, 9, 8], [1, 2, 2, 3, 16]]
    print("This will be a failing test case (We've to Uncomment the next line to verify): ")
    # two_dimensional_array4 = [[13, 11, 2, 4, 6], [14, 2, 20, 20], ["", 4, 3, 10]]

    result1 = find_highest_product(two_dimensional_array1)
    result2 = find_highest_product(two_dimensional_array2)
    result3 = find_highest_product(two_dimensional_array3)
    # We've to Uncomment the next line to verify a test case
    # result4 = find_highest_product(two_dimensional_array4)

    # This will print the highest product of min and max values in each sub-array
    print("First Function:---->")
    print("This is the result 1 of first function: ", result1)
    print("This is the result 2 of first function: ", result2)
    print("This is the result 3 of first function: ", result3)
    # We've to Uncomment the next line to verify a test case
    # print("This is the result 4 of first function: ", result4, " \n\n\n")




    # Function 2
    test_case1 = [[2, 2, 2, 5, 6, 4], [3, 4, 4, 6, 7, 8, 12], [5, 12, 4, 6, 8, 9, 20]]
    print("This will be a failing test case (We've to Uncomment the next line to verify the failing test case): ")
    # test_case2 = [[1, 2, 3], [2, 7, 7, 4, 4, 6, 37, ""], [10, 15, 20, 20]]
    test_case3 = [[3, 3, 3, 5, 6, 4], [3, 6, 4, 6, 7, 8, 12], [5, 8, 12, 12, 12, 5]]
    test_case4 = [[4, 4, 4, 10, 14], [6, 11, 13, 9, 9, 9], [5, 14, 4, 6, 8, 6, 6, 6], [2, 2, 2, 16, 18, 11, 11]]

    print("Second Function:---->")
    print("Test Case 1: ", test_case1)
    test1 = highest_product_pair(test_case1)

    # We've to Uncomment the next two lines to verify a failing test case
    # print("Test Case 2: ", test_case2)
    # test2 = highest_product_pair(test_case2)

    print("Test Case 3: ", test_case3)
    test3 = highest_product_pair(test_case3)
    print("Test Case 4: ",test_case4)
    test4 = highest_product_pair(test_case4)

    # This will print the highest product of min and max values in each sub-array
    print("This is the result of test case 1 of Second function: ", test1)
    # We've to Uncomment the next line to verify a failing test case
    # print("This is the result of test case 2 of Second function: ", test2)
    print("This is the result of test case 3 of Second function: ", test3)
    print("This is the result of test case 4 of Second function: ", test4, " \n")


main()
