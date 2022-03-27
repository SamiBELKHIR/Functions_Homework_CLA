#Write a Python function to fin the max in a list.
l=[1,2,2,4,35,3,999,48,24,3]
n=len(l)
k=l[0]
x=l[0]
def max(l,k):
    n=len(l)
    k=l[0]
    x=l[0]
    for i in range(n-1):
        if l[i+1]>k:
            k=l[i+1]
        if l[i+1]<x:
            x=l[i+1]
    print(k,x)
max(l,k)