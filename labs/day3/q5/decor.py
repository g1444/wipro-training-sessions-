import time
def function_time(func):
    start=0.0
    depth=0
    def wrapper(*args,**kwarws):
        nonlocal start,depth
        if depth==0:
            start=time.time()
        depth+=1
        result=func(*args)
        depth-=1
        if depth==0:
            end=time.time()
            print(f"function '{func.__name__}' executed in {end-start:.3f} seconds")
        return result
    return wrapper