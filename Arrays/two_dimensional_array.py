# Day 1 ⇒ 11, 20, 56, 20
# Day 2 ⇒ 24, 25, 30, 20
# Day3 ⇒ 26, 22, 42, 36
# Day3 ⇒ 26, 22, 42, 36

import numpy as np

twoDArray = np.array([[11, 20, 56, 20],
                      [24, 25, 30, 20],
                      [26, 22, 42, 36],
                      [27, 29, 45, 50]])
print(twoDArray)

# Inserting elements in two dimensional array
newTwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=1)
print(newTwoDArray)

newTwoDArray_ = np.insert(twoDArray, 0, [[1, 5, 3, 4]], axis=0)
print(newTwoDArray_)


def accessElement(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print("Incorrect Index")
    else:
        print(array[rowIndex][colIndex])


accessElement(newTwoDArray, 2, 3)


def traverselTwoADarry(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


traverselTwoADarry(newTwoDArray)


def searchElement(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return "The value is located at index " + str(i) + " " + str(j)
    return "The element not found"


print(searchElement(newTwoDArray, 4))

print("Deleting from two dimensional array")
# Delete row from two dimensional array
new_del_array = np.delete(newTwoDArray, 0, axis=0)
print(newTwoDArray)
print("\n")
print(new_del_array)
