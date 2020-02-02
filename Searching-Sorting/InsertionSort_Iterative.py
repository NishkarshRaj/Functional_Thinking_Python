# Insertion Sort
'''
Online, Inplace sort
Add one element and place it in the right position
Note: First element is already sorted
'''

print("Enter Array as space separated values: ")
array = list(map(int,input().split(' ')))

# Insertion Sort
for i in range(1,len(array)):
    key = array[i]
    j=i-1
    # First find the position the key is to be inserted by moving each greater element one position forward
    while (j>=0) and (key<array[j]):
        array[j+1],array[j] = array[j],array[j+1]
        j = j-1
    # Place the key value in place
    array[j+1]=key
    
# Display Sorted Array 
print(array)
