def fibbanoci():
    a,b=0,1
    while True:
        yield a
        a,b=b,b+a
x=10
fib_gen=fibbanoci()
f=[next(fib_gen) for _ in range(10)]
print(f)