# Bubble Sort
'''
Simplest Sorting Algorithm
Here, no element is set as pivot, trace entire array in both loops!!
Compare adjacent element and replace if wrong order.
'''

print("Enter Array as space separated values: ")
array = list(map(int,input().split(' ')))

for i in range(len(array)):
    for j in range(len(array)-1):
        if(array[j+1]<array[j]):
            array[j], array[j+1] = array[j+1], array[j] 
    
print(array)
