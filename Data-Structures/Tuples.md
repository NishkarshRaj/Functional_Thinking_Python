# Tuples

## Table of contents

1. Creation of Tuples
2. Indexing of Tuples
3. Accessing elements of Tuples
4. Slicing
5. Built in Functions
6. Combine multiple tuples
7. Modify components

**Tuple:** Ordered collection of heterogenous objects.
* Tuples are immutable.
* Tuples are enclosed in () braces

**1. Creation of tuples**
```Python
tuple_variable = tuple() # Empty Tuple creation
tuple_variable = (<<comma separated tuple elements>>)
print(tuple_name)
```

**2. Indexing in tuples**

Positive and negative indexing

Negative indexing for kth positive index = k-n

**3. Access components of tuples**
* tuplename[index]
* Cannot modify because tuples are immutable

**4. Slicing** (Access multiple elements of tuple at once)
> tuple[x:y] 

x inclusive and y exclusive

Elements are extracted from x to y-1

* Slicing always from left to right irrespective of indexing!!!

[:y] -> 0 to y-1

[x:] -> x to -1

**5. Built in functions**
* len(tuplename)
* min(tuplename)
* max(tuplename)

**6. Combine multiple tuples** 

> Tuples are immutable -> either directly print or store in another tuple

* tuple1+tuple2
* tuple1.append(tuple2)

**7. Update Tuples**

We can modify tuples by converting them to lists, modifying the element and converting them back to tuples.
