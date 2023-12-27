# Accessing/Traversing the list
import random
shoppingList = ['Milk', 'Cheese', 'Butter']
print(shoppingList[1])
print('Milk' in shoppingList)

for i in shoppingList:
    print(i)

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i] + "+"
    print(shoppingList[i])

# Update/Insert - List
my_list = [1, 2, 3, 4, 5, 6, 7]
print(my_list)
my_list[2] = 33
print(my_list)

# Insert element in the list
# Insert at the beginning of list
my_list.insert(0, 11)
print(my_list)

# Insert in the middle of list
my_list.insert(4, 30)
print(my_list)

# Insert at the end of list
my_list.append(55)
print(my_list)

# extend a list with another list (add list to other list)
new_list = [11, 12, 13]
my_list.extend(new_list)
print(my_list)

# Deleting from the list
myList = ['a', 'b', 'c', 'd', 'e', 'f']
print(myList)
# Slice
print(myList[0:2])
print(myList[1:])

# update with slice
myList[0:2] = ['x', 'y']
print(myList)

# Delete with pop() method
myList.pop(2)  # at specific index
print(myList)

myList.pop()  # at the end of list
print(myList)

# Delete with del(): this can be used to delete multiple element
# Delete one element
del myList[1]
print(myList)

# Delete multiple element
myList_ = ['a', 'b', 'c', 'd', 'e', 'f']
print(myList_)
del myList_[0:3]
print(myList_)

# Deleting element using remove() this take value it is not based on index
myList_.remove('f')
print(myList_)

# Searching for an element in the list
my_int_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 50
# in operator
if target in my_int_list:
    print(f"{target} is in the list")
else:
    print(f"{target} is not in the list")

# Linear search


def linear_search(list, target):
    for i, value in enumerate(list):
        if value == target:
            return i
    return -1


print(linear_search(my_int_list, 40))

# =============================================
# List Operations and Functions
# =============================================
print("\n List Operations and Functions \n")
a = [1, 2, 3]
b = [4, 5, 6, 7]
c = a + b
print(c)

# * operator
zeros = [0]
zeros = zeros * 4
print(zeros)

dump_ar = [0, 1]
dump_ar = dump_ar * 4
print(dump_ar)

# Lenght of list
print(len(dump_ar))

op_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(max(op_list))
print(min(op_list))
print(sum(op_list))

# Task
# total = 0
# count = 0
# while (True):
#     inp = input("Enter a Number: ")
#     if inp == 'done':
#         break
#     value = float(inp)
#     total = total + value
#     count = count + 1
#     average = total / count

# print('Average ', average)

# Use List and List function to complete the task
# inputs = input("Enter the list of values: ").split(',')
# inputs = [float(input) for input in inputs]
# avg = sum(inputs) / len(inputs)
# print(avg)

# Use list to store value
# inputs_list = list()
# while (True):
#     inp = input("Enter a Number: ")
#     if inp == 'done':
#         break
#     value = float(inp)
#     inputs_list.append(value)
# average = sum(inputs_list) / len(inputs_list)

# print('Average ', average)

# =========================
#  Strings and List
# =========================

string = "12, 23, 45, 56"
list_ = string.split(",")
print(list_)
delimiter = ','
# Joint to join list after spltting it
print(delimiter.join(list_))

# =================================
#   List Comprehension
# =================================
prev_list = [-1, 10, -20, 2, -90, 60, 45, 20]
new_list = [num for num in prev_list if num > 0]
print(new_list)

# Change negative to 0


def get_number(number):
    return number if number > 0 else 0


newList = [get_number(num) for num in prev_list]

# newList = [num if num > 0 else 0 for num in prev_list]

print(newList)

sentence = "My name is Patrick"


def is_consonant(letter):
    vowels = "aeiou"
    return letter.isalpha() and letter.lower() not in vowels


print(is_consonant('a'))

consonants = [letter for letter in sentence if is_consonant(letter)]
print(consonants)

a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a[::2])  # from index 0 to index n and step 2

# to shuffle the list
fruit = ['apple', 'banana', 'papaya', 'cherry']
random.shuffle(fruit)
print(fruit)


def f(value, values):
    v = 1
    values[0] = 44


t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])

# =================
ar = [1, 2, 3, 4, 5]
print(ar[3:0:-1])

# =================
arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]
for i in range(0, 6):
    print(arr[i], end=" ")
