class calculator:
    def add(self,a,b):
        print("basic add:",a+b)
class advanced_calculator(calculator):
    def add(self,a,b):
        print("advanced add:",(a+b)*2)
c1=calculator()
c2=advanced_calculator()
c1.add(23,45)
c2.add(23,45)


def operator(obj):
    print(obj.__class__.__name__)
    obj.add(23,45)
    
operator(c1)
operator(c2)