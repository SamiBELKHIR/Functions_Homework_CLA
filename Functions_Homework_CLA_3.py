#Write a Python function to check whether a number is in a given range.
#first we input range boundatries 
a=int(input('please enter your left boundarie '))
b= int(input('please enter your right boundarie' ))
number = int(input('please enter your number'))
if number in range(a,b):
    print('yes it is indeed')
else:
    print('your numbe is not in this range')