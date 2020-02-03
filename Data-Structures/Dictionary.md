# Dictionaries

## Table of Contents

1. Creation of Dictionaries
2. Accessing elements/components
3. Modifying components

**Dictionary**
* "Hash table" data structures
* Key-value pairs
* Dictionary are enclosed in {}

> Keys are unique values are not

**1. Creation of Dictionary**

dictionary_name = {keys:values , }

* keys: generally numbers or string
* values: any python data type

print(dictionary_name)

**2. Accessing components of dictionary**

* Accessed using keys not index: dict[keys]
* Access all the keys: dict.keys()
* Access all values from dictionary: dict.values()
* Access all elements of dictionary: dict.items()

> Difference between print(dict) and print(dict.items()) -> dict shows dictionary in the form of creation but items shows each key value pair in form of tuples

**3. Modifying elements of dictionaries:** dictionaries are mutable

* Adding a new key-value pair of modifying key-valye pair depending on key passed is in dictionary or not.

**Way 1:** dict[key] = value => example: dict["string"] = value

**Way 2:** dict.update({key:value}) => example: dict.update({"string":value})

* Deleting elements from the dictionary

**Way 1:** Using the del operator: del dict[keys]

* Removing all elements of the dictionary: dict.clear() -> null dictionary (check on print)
