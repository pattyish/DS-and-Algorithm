# ==============================
#   Dictionary Practices
# ==============================
# Define a function to count the frequency of words in a given list of words.
# Example:
# words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
# count_word_frequency(words)
# Output: {'apple': 3, 'orange': 2, 'banana': 1}
words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']


def countWordFrequency(words):
    wordFrequency = {}
    for word in words:
        if word not in wordFrequency:
            wordFrequency[word] = 1
        else:
            wordFrequency[word] = wordFrequency[word] + 1
    return wordFrequency


print(countWordFrequency(words))

# Or this way


def count_word_frequency(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


print(count_word_frequency(words))

# Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.
# Example:
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 3, 'c': 4, 'd': 5}
# merge_dicts(dict1, dict2)
# Output:{'a': 1, 'b': 5, 'c': 7, 'd': 5}

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}


def mergeDicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result


print(mergeDicts(dict1, dict2))

# Another way


def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] = result[key] + value
        result[key] = value
    return result


print(merge_dicts(dict1, dict2))


# Define a function which takes a dictionary as a parameter
#  and returns the key with the highest value in a dictionary.
# Example:
# my_dict = {'a': 5, 'b': 9, 'c': 2}
# max_value_key(my_dict))
# Output:b
my_dict = {'a': 5, 'b': 9, 'c': 2}


def maxValueKey(my_dict):
    dict = my_dict.copy()
    max_key = ""
    max = 0
    for key, value in dict.items():
        if value > max:
            max = value
            max_key = key
    return max_key


print(maxValueKey(my_dict))

# or simple way


def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)


print(max_value_key(my_dict))

# Define a function which takes as a parameter dictionary and
# returns a dictionary in which everse the key-value pairs are reversed.
# Example:
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# reverse_dict(my_dict)
# Output:{1: 'a', 2: 'b', 3: 'c'}
my_dict = {'a': 1, 'b': 2, 'c': 3}


def reverse_dict(my_dict):
    new_dict = my_dict.copy()
    return {value: key for key, value in new_dict.items()}


print(reverse_dict(my_dict))

# Define a function that takes a dictionary as a parameter and
# returns a dictionary with elements based on a condition.
# Example:
# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0)
# Output:{'b': 2, 'd': 4}
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


def filter_dict(my_dict, condition=lambda k, v: v % 2 == 0):
    return {k: v for k, v in my_dict.items() if condition(k, v)}


print(filter_dict(my_dict, condition=lambda k, v: v % 2 == 0))

# Define a function which takes two lists as parameters and
# check if two given lists have the same frequency of elements.
# Example:
# list1 = [1, 2, 3, 2, 1]
# list2 = [3, 1, 2, 1, 3]
# check_same_frequency(list1, list2)
# Output:False

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]


def check_same_frequency(list1, list2):
    def count_elements(lst):
        counter = {}
        for element in lst:
            counter[element] = counter.get(element, 0) + 1
        return counter

    return count_elements(list1) == count_elements(list2)


print(check_same_frequency(list1, list2))

# Or use Count() Method


def check_same_frequency(list1, list2):
    def count_elements(lst):
        return {element: lst.count(element) for element in lst}

    return count_elements(list1) == count_elements(list2)


print(check_same_frequency(list1, list2))
