import time 
def function_time_dec(func):
    def wrapper(*args,**kwargs):
        start=0.0
        depth=0
        if depth==0:
            start=time.time()
        depth+=1
        result=func(*args,**kwargs)
        depth-=1
        if depth==0:
            end=time.time()
            print(f"the time taken for the {func.__name__} is{end-start:.9f}")
        return result
    return wrapper

@function_time_dec
def a(c,b):
    print(c+b)

a(200000000000,555555555598)
