data=[1,2,3,4,5,6,2,4]
s=set(data)
d={x:x*x*x for x in s}
print(d)