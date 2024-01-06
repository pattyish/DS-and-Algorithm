# A dictionary is a collection which is unordered, changeable and indexed
# Create Dictionary
my_dict = dict()
print(my_dict)

# or
my_dict1 = {}
print(my_dict1)

# create with data
my_dictionary = dict(key1="value1", key2="value2")

# Example:
eng_es = dict(one="uno", two="dos", three="tres")
print(eng_es)

# or
my_dictionary = {"key1": "value1", "key2": "value2"}
eng_es = {"one": "uno", "two": "dos", "three": "tres"}
print(eng_es)

# Use list of tuples to create dictionary
eng_es = [("one", "uno"), ("two", "dos"), ("three", "tres")]
my_dict_ = dict(eng_es)
print(my_dict_)

# Update / add an element to the dictionary (Time and space complexity O(1))
my_dict = {"name": "Edy", "age": 26}
print(my_dict)
my_dict["age"] = 27
print(my_dict)

# Add value
my_dict["Address"] = "London"
print(my_dict)

# Traversing through a dictionary time complexity O(N)
# Space complexity is O(1) because we are not using memory
myDict = my_dict
print(myDict)


def traverseDict(dict):
    for key in dict:  # ================> O(N)
        print(key, dict[key])  # ========> O(1)


traverseDict(myDict)

# Search Value in dictionary: Tie=me complexity is O(N)


def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return "The value doesn't exist!!"


print(searchDict(myDict, 27))

# Deleting element in dictional
myDict["education"] = "masters"
myDict_del = myDict
print(myDict_del)

# you can delete with del Time and space complexity O(N)
del myDict_del["age"]
print(myDict_del)

# or use pop method
# it Return None when key not found
removed_element = myDict_del.pop("name", None)
print(removed_element)
print(myDict_del)

# Can remove last element by using popitem()
remove_last = myDict_del.popitem()
print(remove_last)
print(myDict_del)

# Delete everything in dictionary with clear() Time and space complexity is O(1)
myDict_del.clear()
print(myDict_del)
