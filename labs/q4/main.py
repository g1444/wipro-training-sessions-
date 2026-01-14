from class_employee import employee
e1=employee("arun",2000)
e2=employee("dinesh",2900)
print(e1.salary)
try:
    e2.salary=-2900
except Exception as e:
    print(e)