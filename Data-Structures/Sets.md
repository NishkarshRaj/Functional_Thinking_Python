# Sets in Python

## Table of Content

1. Creation of sets
2. Modify components of sets
3. Set Operations
* Union
* Intersection
* Difference
* Symmetric Difference

**Sets:** Unordered collection of unique items.
Sets are enclosed in {}

**1. Set Creation**
Even if duplicate values passed during creation, only unique elements are taken in consideration.
It is not necessary that set contains values in order that we have defined.

**2. Modify the sets**

* Add elements to the set: setname.add(<<value>>)
* Remove elements from list: setname.discard(<<value>>)
* Remove all elements from list: setname.clear()
> Trying printing the NULL Set :)

**3. Set operations** (Venn Diagram Analogy to understand better)

> Sets are immutable?

**Union:** set1.union(set2)
**Intersection:** set1.intersection(set2)
**Difference:** A-B 
{A.difference(B)} not equals B-A {B.difference(A)}
> A-B = A - A.B
**Symmetric Difference:** A--B == B--A 
Symmetric difference gives the set of elements not common in both => A-B + B-A = A+B - A.B
A.symmetric_difference(B) 
