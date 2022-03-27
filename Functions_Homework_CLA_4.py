#Write a Python function to calculate the factorial of a number (a non-negative integer). 
#The function accepts the number as an argument.
number=int(input('please enter your number'))
factor=number
l=[0]
range_1=int(factor)
def factorial(number, factor):
    for i in range(range_1):
        factor=factor-1
        if factor==0:
            break
        else:
            number=number*factor
    print(number)
factorial(number,factor)
        


