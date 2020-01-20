# Take a numeric input in string format
var = input('Enter a number: ')

# Declare list
list1 = list()

# Convert string into list of characters
for el in var:
    list1.append(el)

# Display lenght of string
# print(len(list1))
    
# Display the count of 1
# print(list1.count('0'))

# Display the count of 0
# print(list1.count('1'))
    
if (list1.count('0') == 1) and (list1.count('1') == len(list1)-1):
    print('One flip can be done by flipping the unique 0')
elif (list1.count('1') == 1) and (list1.count('0') == len(list1)-1):
    print('One flip can be done by flipping the unique 1')
else:
    print('One flip cannot be done for homogenization')
