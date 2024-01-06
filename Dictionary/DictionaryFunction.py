# Dictionary Functions
import random
my_dict = {"name": "Edy", "age": 26, "address": "London",
           "education": "master"}

# Copy() create new diction
dict = my_dict.copy()
print(my_dict)
print(dict)
# Clear()
print(my_dict)
my_dict.clear()
print(my_dict)

# fromKeys(): return new dictionary
# take two parameter, sequence[] and value
# Create dict with same value for all keys
newDict = {}.fromkeys([1, 2, 3, 4], 0)
print(newDict)

# get() Method: take two parameter or one
dict.get("age", 27)
print(dict.get("age", 27))
print(dict.get("age"))

# If key is not found it return the None if no value specified
print(dict.get("City"))
print(dict.get("City", 27))

# Items() Method
print(dict.items())

# Keys() Method
print(dict.keys())

# values() Method
print(dict.values())

# popitmes() move last element
dict.popitem()
print(dict)

# setdefault() Method:
# Syntax: dictionary.setdefault(key, default_value)
print(dict)
print(dict.setdefault("name", "added"))
print(dict)

# pop() Method
print(dict.pop("name", "not"))

# Update function Take diction as parameter it append new dictionary to another dictionary
new_dict = {"a": 1, "b": 2, "c": 3}
print(dict)
dict.update(new_dict)
print(dict)


# ================================================
#        Dictionary Operations Builtin
# ================================================
my_dict = {
    3: "three",
    5: "five",
    9: "nine",
    2: "two",
    1: "one",
    4: "four"
}

# IN / NOT operator ( In operator check keys once you only provided dictionary)
print(3 in my_dict)

# To check in values
print("three" in my_dict.values())

# NOT IN operator
print("ten" not in my_dict.values())

# Len() function : take pair as element
print(len(my_dict))

# all() function: check is all key values all true or not zero
print(all(my_dict))

# Any() function: if any true it return true, if all are false it return false
print(any(my_dict))

# Sorted() function:return list of sorted keys
print(sorted(my_dict))

# =============================================
#           Dictionary Comprehension
# =============================================

# Syntax:
# new_dict = {new_key: new_value for item in list } or
# create new for existing
# new_dict = {new_key: new_value for (key, value) in dict.items()}
# you can use condition in comprehension
# new_dict = {new_key: new_value for (key, value) in dict.items() if condition}
city_names = ['Paris', 'London', 'Rome', 'Berlin', 'Madrid']
# Create dictionary from the list
city_temps = {city: random.randint(20, 30) for city in city_names}
print(city_temps)
# Create dictionary from the dictionary: with city temp is > 25
city_above25 = {city: city_temps[city]
                for city in city_temps if city_temps[city] > 25}
print(city_above25)

# or this way
new_dict = {city: temp for (city, temp) in city_temps.items() if temp > 25}
print(new_dict)
