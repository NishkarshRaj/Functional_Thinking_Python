# Take User Input
print("Enter Array as space separated values: ")
array = list(map(int,input().split(' ')))

# Sort the array for binary searching
array.sort()
print(array)

# Take element to be searched for
el = int(input("Enter element to be searched: "))

low = 0 # Index of first element
high = len(array)-1 # Index of last element
flag = 0 # Default Case
while(low<high):
    mid = int(low+high/2);
    if(el>array[mid]):
        low = mid + 1;
    elif (el<array[mid]):
        high = mid -1
    else:
        flag = 1 # Found the element
        break

if(flag==0):
    print("Element not found")
else:
    print("Element found")
 

