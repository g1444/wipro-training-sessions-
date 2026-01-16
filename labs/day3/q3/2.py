def fibonnaci(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b
fib=fibonnaci(15)
for x in fib:
    print(x)