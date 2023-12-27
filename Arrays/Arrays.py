import numpy as np
import array

# ======= using array module for Python =====
# Empty array
my_array = array.array('i')
print(my_array)

# Array with elements
my_array1 = array.array('i', [1, 2, 3, 4])
print(my_array1)

# ====== Arrays with Numpy =============
np_array = np.array([], dtype=int)
print(np_array)
np_array1 = np.array([1, 2, 3, 4])
print(np_array1)

my_array1.insert(2, 6)
print(my_array1)

# Traversal Array


def traversalArray(array):
    for i in array:
        print(i)


traversalArray(my_array1)


def accessElement(array, index):
    if index >= len(array):
        print("Out of array length")
    else:
        print(f" Element on index is: {array[index]}")


accessElement(my_array1, 7)


def searchElement(array, target):
    for index in range(len(array)):
        if array[index] == target:
            print(f"{target} is in the array")
        else:
            print(f"We can't find {target} is not in Array")


def linearSearch(array, target):
    for index in range(len(array)):
        if array[index] == target:
            return index
    return -1


print(linearSearch(my_array1, 6))

# Removing element
my_array1.remove(6)
print(my_array1)
