# Write a function to find the missing number in a
# given integer array of 1 to 100. The function takes
# to parameter the array and the number of elements that
# needs to be in array.  For example if we want to
# find missing number from 1 to 6 the second parameter will be 6.
# Example
# missing_number([1, 2, 3, 4, 6], 6) # 5

# formula : Sum = n(n + 1)/2
# S represents the sum of the sequence of numbers from 1 to n
# n is the totalCount or the last number in the sequence.

import numpy as np


def missingNumbers(array, arrayLen):
    sumSequence = arrayLen * (arrayLen + 1) / 2
    if sum(array) != sumSequence:
        return sumSequence - sum(array)


print(int(missingNumbers([1, 2, 3, 4, 6], 6)))

# Other way of doing this


def missingNumbers_1(array, arrayLen):
    sumSequence = 0
    for i in range(1, arrayLen + 1):
        sumSequence += i
    missingNumber = sumSequence - sum(array)
    return missingNumber


# print(int(missingNumbers_1([1, 2, 3, 4, 6], 6)))


# Question 2
# Write a Program to find all pairs of integers whose sum is equal
# to given number. show output as an Index of the numbers

# example: nums = [2,3,11,15], target = 9
#          output = [0, 1]
# output: because nums[0] + nums[1] == 9

# Logic questions to ask

# 1. Does array conatins only positive or negative numbers
# 2. what if the same pair repeats twic, should we print it every time
# 3. if the reverse of the pair is acceptable eg. (4,1) and (1, 4),
#    if the given sum is 5
# 4. do we need to print only distinct pairs? does (3, 3) is a valid pair
#    given sum of 6
# 5. How big is the array
def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range((i + 1), len(nums)):
            if nums[i] == nums[j]:
                continue
            if nums[i] + nums[j] == target:
                print(i, j)


nums = [1, 2, 3, 2, 3, 4, 5, 6]
findPairs(nums, 9)

# Another way of doing it


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


nums = [2, 7, 11, 15]
nums = [1, 2, 3, 2, 3, 4, 5, 6]
target = 9
indices = two_sum(nums, target)
print(f"Indices of the two numbers are: {indices}")

# Reversing Array


def reverseArray(nums):
    for i in range(0, int(len(nums)/2)):
        other = len(nums) - i - 1
        temp = nums[i]
        nums[i] = nums[other]
        nums[other] = temp
    print(nums)


reverseArray(nums)
# Question 3 - Check if an array contains a number in Python
# Question To ask:
# 1. Is array numbers sorted or not?
# If it sorted linear search is suitable for task other wise binary search
# could be suitable


numbers_ = range(1, 21)
numbers = np.array(numbers_)


def findNumber(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            print("Number Exist: ", numbers[i])
            break
        else:
            continue


findNumber(numbers, 10)

# Find the maximum product of two integers in
# an array where all elements are positive.
# Example

# arr = [1, 7, 3, 4, 9, 5]
# max_product(arr) # Output: 63 (9*7)
# Easy way to this sort from max to min and take first to big number and
# multiply them


def maximumProduct(array):
    array = sorted(array, reverse=True)
    return array[0] * array[1]


print(maximumProduct(numbers))

# Or this could work


def maxProduct(array):
    maxNum1 = 0
    maxNum2 = 0
    for num in array:
        if num > maxNum1:
            maxNum2 = maxNum1
            maxNum1 = num
        elif num > maxNum2:
            maxNum2 = num
    return maxNum1 * maxNum2


print(f"Product: {maxProduct(numbers)}")

# Write a function called middle that takes a list and
# returns a new list that contains all but the first and last elements.

# myList = [1, 2, 3, 4]
# middle(myList)  # [2,3]


def middleElements(list):
    return list[1:len(list) - 1]  # or list[1:-1]


print(numbers.tolist())
print(middleElements(numbers.tolist()))

# Or this way


def middle(list):
    newList = []
    for i in range(1, len(list)):
        newList.append(list[i])
    return newList


print(numbers.tolist())
print(middleElements(numbers.tolist()))

# Given 2D list calculate the sum of diagonal elements.
# Example
# myList2D= [[1,2,3],[4,5,6],[7,8,9]]
# diagonal_sum(myList2D) # 15


def diagonalSum(list2D):
    sum = 0
    for row in range(len(list2D)):
        for col in range(len(list2D[0])):
            if row == col:
                sum += list2D[row][col]
            else:
                continue
    return sum


myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Diagonal Product: {diagonalSum(myList2D)}")

# Can also iterate through Matrix


def diagonal_sum(matrix):
    # Initialize the sum to 0
    total = 0
    # Iterate through the rows of the matrix
    for i in range(len(matrix)):
        # Add the diagonal element to the total sum
        total += matrix[i][i]
    return total


print(f"Diagonal Product: {diagonal_sum(myList2D)}")

# Given a list, write a function to get first, second best scores
# from the list. List may contain duplicates.
# Example

# myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
# first_second(myList) # 90 87


def first_second(my_list):
    unique_scores = list(set(my_list))
    my_list = sorted(unique_scores, reverse=True)
    return my_list[0], my_list[1]


myList = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second(myList))

# Other ways


def first_second(my_list):
    max1, max2 = float('-inf'), float('-inf')
    for num in my_list:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num
    return max1, max2


my_list = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second(my_list))  # Output: (90, 87)

# Write a function to remove the duplicate numbers on given
# integer array/list.
# Example

# remove_duplicates([1, 1, 2, 2, 3, 4, 5])
# Output : [1, 2, 3, 4, 5]


def removeDuplicate(list):
    newList = []
    for i in list:
        if i not in newList:
            newList.append(i)
    return newList


print(removeDuplicate([1, 1, 2, 2, 3, 4, 5]))

# Write a function to find all pairs of an integer array whose sum is
# equal to a given number. Do not consider commutative pairs.

# Example

# pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
# Output : ['2+5', '4+3', '3+4', '-2+9']


def pair_sum(arr, target_sum):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                result.append(f"{arr[i]}+{arr[j]}")
    return result


arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target_sum = 7
print(pair_sum(arr, target_sum))  # Output: ['2+5', '4+3', '3+4', '-2+9']

# Print unordered Pair list


def printUnorderedList(array):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            print(str(array[i]) + "," + str(array[j]))


printUnorderedList(arr)

# Given an integer array nums, return true if any value appears at
# least twice in the array, and return false if every element is distinct.
# Example :

# Input: nums = [1,2,3,1]
# Output: true
# Hint: Use sets

# First way:


def contains_duplicate(nums):
    containDuplicate = False
    seenNumber = []
    for i in nums:
        if i not in seenNumber:
            seenNumber.append(i)
        else:
            containDuplicate = True
            break
    return containDuplicate


nums = [1, 2, 3, 1]
print(contains_duplicate(nums))

# Or using set


def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# Example usage
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print(containsDuplicate(nums))

# Reversing word


def reverse_word(word):
    reversed_ = ""
    for letter in word:
        reversed_ = letter + reversed_
    print(reversed_)
    return reversed_


reverse_word('shoe')

# Question 6 - Permutation: Check if two give list are permitation or not.


def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    # Sort each list
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False


list1 = [1, 2, 3]
list2 = [1, 3, 2]
print(f"Is Permutation: {permutation(list1, list2)}")

# You are given an n x n 2D matrix representing an image, rotate the image by
# 90 degrees (clockwise). You have to rotate the image in-place, which means
# you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.


def rotate(matrix):
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):  # Iterate over the rows
        for j in range(i, n):  # Iterate over the columns starting from the current row 'i'
            # Swap the elements at positions (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            print(
                f"{i} === {j} == i-j == {matrix[i][j]} == j-i == {matrix[j][i]}")
    # Reverse each row
    for row in matrix:  # Iterate over each row in the matrix
        row.reverse()  # Reverse the elements in the current row


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
for row in matrix:
    print(row)

rotate(matrix)

print("\nMatrix After Rotation:")
for row in matrix:
    print(row)
