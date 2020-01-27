#FizzBuzz Code
# Multiple of 3 -> Fizz
# Multiple of 5 -> Buzz
# Multiple of 5 and 3 -> FizzBuzz

# Logical And && does not work, use and keyword
def fizzbuzz(value):
    for i in range(1,value+1):
        if(i%5==0) and (i%3==0):
            print('FizzBuzz')
        elif (i%3==0):
            print('Fizz')
        elif (i%5==0):
            print('Buzz')
        else:
            print(i)
            
# Driver Code
x = int(input("Enter a number: "))
fizzbuzz(x)
