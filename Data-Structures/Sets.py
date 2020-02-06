set1 = {1,2,3,4,5}

set1.add(6)
print(set1)
set1.discard(6)
print(set1)
set1.clear()
print(set1) # empty object -> object() class

set2 = {1,2,3,4}
set3 = {1,2,5,6}
print(set2.union(set3))
print(set2.intersection(set3))
print(set2.difference(set3))
print(set3.difference(set2))
print(set2.symmetric_difference(set3))

set1 = set2.difference(set3)
print(set1) # Sets are mutable
