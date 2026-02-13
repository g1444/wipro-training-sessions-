def simple_decorator(func):
    def wrapper(*args,**kwargs):
        print("Funtion started")
        return func(*args,**kwargs)
    return wrapper

@simple_decorator
def a(a,b):
    print(a+b)
a(1,2)
