# Write a Python program to reverse a string.
string = input('enter your string ')
rev_string=string [::-1]
print(rev_string)
#second method 
a = input('enter your string ')
a2=''
for i in range(len(a)):
    a3=a[-i-1]
    a2=a2+a3
print(a2)


