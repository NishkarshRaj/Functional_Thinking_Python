# Lambda Function nested in another user defined function

# User Defined function
def Exponent(n):
    return lambda a : a**n

# Take user input for n
n = int(input("Enter a number to become the power of exponent: "))
exp = Exponent(n)

# Take the number to be exponentiated
val = int(input("Enter a number to be exponentiated: "))

# Call the lambda function
print(exp(val))
    