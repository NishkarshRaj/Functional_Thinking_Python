'''Leap Year'''
'''Logic: If a year is divisible by 4 then it is a new year.
Exception: Centuries not divisible by 400 are not leap years
'''

# Take input year
year = int(input("Enter year: "))

# Driver Code
if (year%4==0):
    if (year%100==0):
        if (year%400==0):
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")
