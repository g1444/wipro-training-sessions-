class student:
    name="ravi"
    age=21

s1=student()
print(s1.name)
print(s1.age)

class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
e1=employee("laala",44)
print(e1.name,e1.age)