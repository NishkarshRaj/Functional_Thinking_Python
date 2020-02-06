'''
Question: Take whole list at once and then find its second maximum element
'''
list1 = list()
count = int(input('Enter the number of element: '))
list1 = list(map(int,input().split(' '))) 
# Remove will not work on list if max is duplicate
# Convert to set
set1 = set(list1)
set1.remove(max(set1)) 
print(max(set1))
