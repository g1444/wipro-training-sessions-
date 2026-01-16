from abc import ABC,abstractmethod

class employee(ABC):
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @abstractmethod
    def salary(self):
        pass
class emp(employee):
    
    def salary(self):
        print(self.name,self.age,00000)

e=emp("dinesh",25)
e.salary()

