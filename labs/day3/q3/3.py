l=[91,2,3,4,54]
i=iter(l)
for _ in i:
    print(_)
print("\n")

def gen(n):
    for x in range(1,n+1):
        yield x
for _ in gen(10):
    print(_)