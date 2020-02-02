# Selection Sort, on each iteration, put the minimum element to the left

print("Enter Array as space separated values: ")
array = list(map(int,input().split(' ')))

for i in range(len(array)-1):
    pos_min = i 
    for j in range(i+1,len(array)):
        if(array[pos_min]>array[j]):
            pos_min = j
    array[i], array[pos_min] = array[pos_min], array[i] 
    
print(array)
