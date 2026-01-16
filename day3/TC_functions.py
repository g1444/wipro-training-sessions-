# basic syntax of a function is 
# def name(arg1,arg2,. . . . ):
#   process
#   return type
def add(a,b):
    print(a+b)
    return

def sub(a,b):
    return a-b
print(add(3,4))
print(sub(9,3))

def gt(greetings="hello", name="gowtham"):
    print("%s,%s"%(greetings,name))
gt("oye")

def params(*params):
    print(params)

params("gowtham here")
params(1,2.3,4,5,5,6,7,7)

def params1(**params):
    print(params)
params1(x=1,y=4,z=929)