# Take a numeric input in string format
var = input('Enter a number: ')

# Declare list
list1 = list()

# Convert string into list of characters
for el in var:
    list1.append(el)

if (list1.count('0') == 1):
    print('One flip can be done by flipping the unique 0')
elif (list1.count('1') == 1):
    print('One flip can be done by flipping the unique 1')
else:
    print('One flip cannot be done for homogenization')
