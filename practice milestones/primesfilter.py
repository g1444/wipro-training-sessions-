l=[1,3,2,5,7,8,9,19,23]
p=list(
    filter(lambda x:x>1 and all(x%i!=0 for i in range(2,int(x**0.5)+1)),l))
print(p)