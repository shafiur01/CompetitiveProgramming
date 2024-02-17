def divisorSubstrings(num: int, k: int):
    # initialize a variable (number_of_k_beauty) to store the number of k-beauty numbers.
    # we have to traverse the num in such a way that it takes k number of digits from num at a time and see if that thing divides the whole number
    # so we have to convert the num into string for the traversal
    # then we take k number of string while traversing and convert them into int again so that we can use them for dividing the int(num) and see if that's a divisor of num or not. If it is then we increase the number_of_k_beauty variable everytime we find that it can divide the num

    number_of_k_beauty = 0
    num_string = str(num)

    for i in range(len(num_string)):
        if i + k <= len(num_string):
            int_probable_k_beauty = int(num_string[i:i + k])
            if (int_probable_k_beauty != 0) and (num % int_probable_k_beauty) == 0:
                number_of_k_beauty += 1
            else:
                continue
        else:
            break
    return number_of_k_beauty


print(divisorSubstrings(430043, 2))