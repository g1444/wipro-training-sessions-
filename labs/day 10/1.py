a=10
b=0

try:
        print(a/b) 
except:
    print(ZeroDivisionError)
finally:
    print("this problem is over")