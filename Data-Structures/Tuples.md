Overview
1. Creation of Tuples
2. Indexing of Tuples
3. Accessing elements of Tuples
4. Slicing
5. Built in Functions
6. Combine multiple tuples
7. Modify components

-----------------------------------------------------------

Tuple: Ordered collection of heterogenous objects.
Tuples are immutable.
Tuples are enclosed in () braces

1. Creation of tuples
-> print(tuple_name)

2. Indexing in tuples
Positive and negative indexing again -> Negative indexing for kth positive index = k-n

3. Access components of tuples
-> tuplename[index]
* Cannot modify

4. Slicing (Access multiple elements of tuple at once)
tuple[x:y] 
x inclusive and y exclusive
Elements are extracted from x to y-1
* Slicing always from left to right irrespective of indexing!!!
[:y] -> 0 to y-1
[x:] -> x to -1

5. Built in functions
* len(tuplename)
* min(tuplename)
* max(tuplename)

6. Combine multiple tuples [Remember it is immutable -> either directly print or store in another tuple]
* tuple1+tuple2
* tuple1.append(tuple2)

7. Update Tuples
BCD!!! You are stupid if you say I cannot update tuples because you can if you know more!!!
Convert to list -> Update -> Convert to Tuple 
