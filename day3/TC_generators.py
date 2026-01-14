def number(a,b):
    yield a
    yield b
    yield a+b
gen=number(234,445)
print(next(gen))
print(next(gen))
print(next(gen))

# example
def count_up(n):
    for i in range(1,n+1):
        yield i
for val in count_up(4):
    print(val)