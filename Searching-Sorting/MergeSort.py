# Merge Sort
'''
Divide and Conquer Algorithm
-> Divide: Divide equally until one element: each individual element is sorted
-> Conquer: Combine elements by comparing
'''

# Conquer
def merge(arr,low,mid,high):
    # Create two arrays for two halves
    n1 = mid - low + 1;
    n2 = high - mid;
    # Declaring empty arrays
    Left = list()
    Right = list()
    for i in range(n1):
        Left.append(0)
    for j in range(n2):
        Right.append(0)    
    # Creating left array
    for i in range(0,n1):
        Left[i] = arr[low+i]
    # Creating right array
    for j in range(0,n2):
        Right[j] = arr[mid+1+j]
    # Merging Both arrays
    i=0
    j=0
    k=low
    while (i<n1) and (j<n2):
        if(Left[i]<=Right[j]):
            arr[k]=Left[i]
            i = i+i
        else:
            arr[k]=Right[j]
            j = j+1
        k=k+1
    # Adding left over elements from both array if any
    while(i<n1):
        arr[k]=Left[i]
        i=i+1
        k=k+1
    while(j<n2):
        arr[k]=Right[j]
        j=j+1
        k=k+1
    
# Divide
def mergesort(array,low,high):
    if(low<high):
        mid = int((low+high)/2)
        mergesort(array,low,mid)
        mergesort(array,mid+1,high)
        merge(array,low,mid,high)

# Driver Code
print("Enter Array as space separated values: ")
array = list(map(int,input().split(' ')))
high = len(array)-1
mergesort(array,0,high)
    
# Display Sorted Array 
print(array)
