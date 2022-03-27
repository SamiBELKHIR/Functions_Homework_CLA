#Write a Python function to sum all the numbers in a list.
l=[1,2,3]
sum1=0
def sum(l,sum1):
    for i in l:
        sum1=sum1+i
    print(sum1)
sum(l,sum1)