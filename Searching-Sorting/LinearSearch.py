import numpy as np

print("Enter Array as space separated values: ")
arr = list(map(int,input().split(' ')))
    
# Convert to Array
array = np.array(arr)
print(array)

# Take element to be searched
el = int(input("Enter element to be searched: "))

# Searching, if found flag = 1 else flag = -1
flag = -1
for x in array:
    if x == el:
        flag = 1
    
if(flag==1):
    print("Element Found")
else:
    print("Element does not exists in the array")
