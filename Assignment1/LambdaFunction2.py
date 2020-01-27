# lambda function with 3 input

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))

# Creating the lambda function 
a = lambda x,y,z : x + y + z

print(a(x,y,z))
