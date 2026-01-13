data=[1,2,3,4,5,6,2,4]
sqd=[x*x for x in data]
print(sqd)
s=[i for i in sqd if i%2==0]
print(set(s))