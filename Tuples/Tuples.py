# How to create Tubles
newTuple = ("a", "b", "c", "d", "e")
print(newTuple)

# to initialize tuble with one element
tuple_init = ("a", )
print(tuple_init)

# or use Tuple function to create tuple
newTuple1 = tuple()  # For empty
newTuple1 = tuple("abcde")
print(newTuple1)

# How to access Tuple element
newTuple = ("a", "b", "c", "d", "e")
print(newTuple[-1])

# slice[:] operators
print(newTuple[1:4])

# How to traverse throuh Tuple
newTuple = ("a", "b", "c", "d", "e")

for i in newTuple:
    print(i)

# or
for i in range(len(newTuple)):
    print(newTuple[i])

# To search element in Tuple
# Using in operator
newTuple = ("a", "b", "c", "d", "e")
print("a" in newTuple)  # ================> O(N)

# Using index method
print(newTuple.index("b"))  # it give index of element if is in tuples
# It raise the error if element is not in tuples time complexity is O(N)

# custom way


def searchTuple(p_tuple, element):
    for i in range(0, len(p_tuple)):
        if p_tuple[i] == element:
            return f"Element is found at {i} index"
    return "The element is not found"


print(searchTuple(newTuple, "b"))

# ========================================
#      Tuple Operations/Functions
# ========================================
myTuple = (1, 4, 3, 2, 5)
myTuple1 = (1, 2, 6, 9, 8, 7)

print(myTuple)
print(myTuple1)

# Concatenate tuples with + sign
print(myTuple + myTuple1)

# Using * sign to replicate tuple n times:
# every element in tuple appear n times in new tuple
print(myTuple * 2)

# In operator
print(4 in myTuple)

# ===================================
#        Functions
# ===================================
# Tuple doesn't have many functions because it is immutable
# you cannot add, remove, update element on tuple

# Count(): it count frequence of give element appeared in tuple
myTuple = (1, 4, 3, 2, 5, 2)
print(myTuple.count(2))

# Index(): show the index of element
print(myTuple.index(4))

# len() function: show the size of tuple
print(len(myTuple))

# Max() and Min(): to get maximum and minimun
print(f"Maximum is:  {max(myTuple)}")
print(f"Minimum is:  {min(myTuple)}")

# Tuple(): this can be used to convert list into tuple
print(tuple([1, 2, 3, 4, 5, 6, 7, 8, 9]))
