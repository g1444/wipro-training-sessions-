from positive import positive_salary
class employee:
    salary=positive_salary()
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    

e1=employee("arun",2000)
e2=employee("dinesh",2900)
print(e1.salary)
try:
    e2.salary=-2900
except Exception as e:
    print(e)