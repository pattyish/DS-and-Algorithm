# Write a function that calculates the sum and
# product of all elements in a tuple of numbers.
# Example
# input_tuple = (1, 2, 3, 4)
# sum_result, product_result = sum_product(input_tuple)
# print(sum_result, product_result)  # Expected output: 10, 24
input_tuple = (1, 2, 3, 4)


def sum_product(input_tuple):
    prod_result = 1
    for i in range(0, len(input_tuple)):
        prod_result *= input_tuple[i]
    return sum(input_tuple), prod_result


sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)

# Or this way


def sum_product(t):
    sum_result = 0
    product_result = 1

    for num in t:
        sum_result += num
        product_result *= num

    return sum_result, product_result


sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)

# Create a function that takes two tuples and returns a tuple containing
# the element-wise sum of the input tuples.
# Example
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# output_tuple = tuple_elementwise_sum(tuple1, tuple2)
# print(output_tuple)  # Expected output: (5, 7, 9)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)


def tuple_elementwise_sum(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Input tuples must have the same length.")
    # Zip() match the element on same index and create pair, put them together in list
    # Map(sum) map each pair and calculate sum
    return tuple(map(sum, zip(tuple1, tuple2)))


output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple)

# Another way


def tuple_elementwise_sum_(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Input tuples must have the same length.")
    output_list = []
    for i in range(len(tuple1)):
        output_list.append(tuple1[i] + tuple2[i])
    return tuple(output_list)


output_tuple = tuple_elementwise_sum_(tuple1, tuple2)
print(output_tuple)

# using tuple comprehension


def tuple_elementwise_sum(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Input tuples must have the same length.")
    return tuple(x + y for x, y in zip(tuple1, tuple2))


output_tuple = tuple_elementwise_sum_(tuple1, tuple2)
print(output_tuple)

# Using lambda function


def tuple_elementwise_sum(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Input tuples must have the same length.")
    return tuple(map(lambda x, y: x + y, tuple1, tuple2))


output_tuple = tuple_elementwise_sum_(tuple1, tuple2)
print(output_tuple)

# Write a function that takes a tuple and a value, and returns a new tuple
# with the value inserted at the beginning of the original tuple.
# Example
# input_tuple = (2, 3, 4)
# value_to_insert = 1
# output_tuple = insert_value_front(input_tuple, value_to_insert)
# print(output_tuple)  # Expected output: (1, 2, 3, 4)

input_tuple = (2, 3, 4)
value_to_insert = 1


def insert_value_front(input_tuple, value_to_insert):
    list_ = [value_to_insert]
    for i in input_tuple:
        list_.append(i)
    return tuple(list_)


output_tuple = insert_value_front(input_tuple, value_to_insert)
print(output_tuple)

# Another way: using tuple concatination


def insert_value_at_beginning(input_tuple, value_to_insert):
    return (value_to_insert,) + input_tuple


output_tuple = insert_value_at_beginning(input_tuple, value_to_insert)
print(output_tuple)

# Write a function that takes a tuple of strings and concatenates them,
# separating each string with a space.
# Example
# input_tuple = ('Hello', 'World', 'from', 'Python')
# output_string = concatenate_strings(input_tuple)
# print(output_string)  # Expected output: 'Hello World from Python'

input_tuple = ('Hello', 'World', 'from', 'Python')


def concatenate_strings(input_tuple):
    output = ""
    for i in range(len(input_tuple)):
        output += input_tuple[i]
        if i != len(input_tuple) - 1:
            output += " "
    return output


output_string = concatenate_strings(input_tuple)
print(output_string)

# Simple way using join()


def concatenate_strings(input_tuple):
    return ' '.join(input_tuple)


output_string = concatenate_strings(input_tuple)
print(output_string)

# Create a function that takes a tuple of tuples and
# returns a tuple containing the diagonal elements of the input.
# Example
# input_tuple = (
#     (1, 2, 3),
#     (4, 5, 6),
#     (7, 8, 9)
# )
# output_tuple = get_diagonal(input_tuple)
# print(output_tuple)  # Expected output: (1, 5, 9)

input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# Time complexity O(N*M) or O(N2)


def get_diagonal(input_tuple):
    diagonal = []
    for row in range(0, len(input_tuple)):
        for col in range(0, len(input_tuple[0])):
            if row == col:
                diagonal.append(input_tuple[row][col])
    return tuple(diagonal)


output_tuple = get_diagonal(input_tuple)
print(output_tuple)

# Using Comprehension way:

# Time complexity O(N)


def get_diagonal(input_tuple):
    return tuple(input_tuple[i][i] for i in range(len(input_tuple)))


print(range(len(input_tuple)))
output_tuple = get_diagonal(input_tuple)
print(output_tuple)

# Write a function that takes two tuples and returns a tuple containing
# the common elements of the input tuples.
# Example
# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (4, 5, 6, 7, 8)
# output_tuple = common_elements(tuple1, tuple2)
# print(output_tuple)  # Expected output: (4, 5)

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)


def common_elements(tuple1, tuple2):
    return tuple(x for x in tuple1 if x in tuple1 and x in tuple2)


output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)

# or using set


def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))


output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)
