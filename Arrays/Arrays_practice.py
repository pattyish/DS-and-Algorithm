from array import *

# 1. Create an array and traverse

my_array = array('i', [1, 2, 3, 4, 5])

for i in my_array:
    print(i)

# 2. Access individual elements throught indexes
print(my_array[3])

# 3. Append any value in an arrau using append() Method
# This work only to add at the end of array
my_array.append(6)
print(my_array)

# 4. Insert value in an array using insert() method:
# Time consuming O(N) but flexible to insert on any index you wan
my_array.insert(0, 11)
print(my_array)

my_array.insert(3, 12)
print(my_array)

# 5. Extend python array using extend() method
# Adding more than one value in array: It takes array of elements
new_array = array('i', [13, 14, 15])
my_array.extend(new_array)
print(my_array)

# 6. Add items from list into array using fromlist() method
tempList = [20, 21, 22]
my_array.fromlist(tempList)
print(my_array)

# 7. Remove any array element using remove() method
# This remove the fisrt value and stop: in case value is duplicate in array
my_array.remove(22)
print(my_array)

# 8. Remove last array element using pop() method: time efficient
my_array.pop()
print(my_array)

# 9. Fetch any element throught its index using index() method
print(my_array.index(20))

# 10. Reverse a Python array using reverse() method
my_array.reverse()
print(my_array)

# 11. Get array buffer information through buffer_info() method
print(my_array.buffer_info())

# 12. check for number of occurences of an element using count() method
print(my_array.count(11))

# 13. Convert array to string using tostring() method
strTemp = my_array.tobytes()
print(strTemp)
ints = array('i')
ints.frombytes(strTemp)
print(ints)

# 14. Convert array to a python list with same elements using tolist() method
# print(my_array.tolist())

# 15. Slice Element from an array
print(my_array[::-1])
print(my_array[-3])
print(my_array[2:])
