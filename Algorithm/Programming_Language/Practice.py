from functools import reduce

# Helper function to check if a number is prime
def is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


# A helper function to return a recursive lambda
def make_recursive_lambda(f):
    return lambda n, start=2: f(f, n, start)


# The recursive lambda function that computes prime factors
prime_factors = make_recursive_lambda(lambda self, n, start: [] if n == 1 else
                [start] + self(self, n // start, start) if n % start == 0 else
                self(self, n, next(filter(lambda x: n % x == 0, range(start + 1, int(n ** 0.5) + 1)), n)))


# Function to check if the number is semiprime
def is_semiprime(n):
    factors = prime_factors(n)
    return len(factors) == 2 and factors[0] * factors[1] == n


# Rest of the functions remain unchanged
# Function to flatten a matrix
def flatten_matrix(matrix):
    return reduce(lambda x, y: x + y, matrix)


# Function to categorize numbers
def categorize_numbers(matrix):
    flat_matrix = flatten_matrix(matrix)
    primes = list(filter(is_prime, flat_matrix))
    print("The prime set: ", primes)

    semiprimes = list(filter(is_semiprime, flat_matrix))
    print("The semi-prime set: ", semiprimes)

    other_numbers = list(filter(lambda x: x not in primes and x not in semiprimes, flat_matrix))
    print("The other number set is: ", other_numbers)

    return primes, semiprimes, other_numbers


# # Function to find two most common numbers
# def two_most_common(numbers):
#     if not numbers:
#         return (None, None)
#     freq = Counter(numbers).most_common(2)
#     return (freq[0][0], freq[1][0]) if len(freq) > 1 else (freq[0][0], None)






def make_Dict(dict, item):
    if item not in dict.keys():
        dict[item] = 1
    else:
        dict[item] += 1
    return dict


def remove_Max_Occurance(dict1):
    # Your dictionary with digits as keys and counts as values

    # Use reduce to find the maximum occurrence
    max_digit = reduce(lambda x, y: x if x[1] > y[1] else y, dict1.items())

    # Now creating a new dictionary without the max occurrence digit
    digit_counts = {digit: count for digit, count in dict1.items() if digit != max_digit[0]}

    # print("Digit with maximum occurrence:", max_digit[0])
    # print("New dictionary without the max occurrence digit:", digit_counts)
    return max_digit[0], digit_counts


# Lambda function to call remove_Max_Occurance twice and store the results
find_two_max_digits = lambda dict1: [remove_Max_Occurance(dict1)[0]] + [remove_Max_Occurance(remove_Max_Occurance(dict1)[1])[0]]


# Calling the lambda function and store the two maximum digits
def two_most_common(array2):
    # making a dictionary to store the digit count of the passed array
    dict1 = dict()

    # filling the dict1 dictionary with the digit, and it's count by calling external function make_Dict from inside the
    # lambda function
    arr3 = list(map(lambda element: make_Dict(dict1, element), array2))

    # making a list by calling a function which will fill the list with most frequent 2 digits from right side
    list1 = find_two_max_digits(dict1)

    # reversing the list to maintain desired sequence
    list1.reverse()

    return list1


# Main function to find the pair with the highest product among the most common
def highest_product_pair(matrix):
    primes, semiprimes, others = categorize_numbers(matrix)

    common_primes = two_most_common(primes)
    print("Common Prime: ", common_primes)

    common_semiprimes = two_most_common(semiprimes)
    print("Common semi-Prime: ", common_semiprimes)

    common_others = two_most_common(others)
    print("Common Other: ", common_others, "\n")

    all_pairs = [common_primes, common_semiprimes, common_others]

    # Reduce to find the pair with the highest product without using max or min
    highest_product_pair = reduce(lambda x, y: x if x[0]*x[1] > y[0]*y[1] else y, all_pairs)

    # Return only the pair without the product
    return highest_product_pair[:2]


# Testing the function
def main():
    test_cases = [
        ([[2,2,2,5,6,4],[3,4,4,6,7,8,12],[5,12,4,6,8,9,20]] , [8, 12]),

        ([[1, 2, 3], [2, 7, 7, 4, 4, 6, 37, 37], [10, 15, 20, 20]], [7,37])]

    for matrix, expected in test_cases:
        result = highest_product_pair(matrix)
        print(f'Input: {matrix}\nExpected: {expected}, Result: {result}\n')


if __name__ == "__main__":
    main()




