# In python, single line comments in #
# Taking integer input with message
# No need to use semi-colons in python, interpreted language
count=int(input('Enter number of elements: '))

# Declare Empty List
list1 = list()
list2 = list()
# Or -> list1 = []

# Take input numbers
for i in range (0,count):
    list1.append(int(input('Enter value: ')))
    list2.append(0) # declare default values     

# Reverse not working :(
'''# Create another list storing reverse values of list 1
list2 = list1.reverse()'''

# Manually created reverse list
c = count-1 # index of list to decrease
for el in list1:
    list2[c] = el
    c=c-1

# Sum of list1 and list2
for i in range (0,count):
    list2[i] = list2[i] + list1[i]
    
# Display the final list
print(list2)    
