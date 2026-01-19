# class Calc:
#     def add(self, *params):
#         total = 0
#         for x in params:
#             total += x
#         return total

# c = Calc()
# print(c.add(2,3))          
# print(c.add(2,3,4))        
# print(c.add(1,2,3,4,5)) 
class Parent:
    def __init__(self):
        print("Parent")

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)   # old-style call
        print("Child")
c=Child()
print(c)