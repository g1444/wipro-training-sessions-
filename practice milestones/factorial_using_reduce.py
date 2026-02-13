from functools import reduce
x=int(input("enter the number: "))
a=1
f=reduce(lambda a,b: a*b,range(1,x+1))
print(f)