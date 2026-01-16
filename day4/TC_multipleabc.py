from abc import ABC,abstractmethod
class bank(ABC):
    @abstractmethod
    def loan(self):
        pass
    @abstractmethod
    def interst(self):
        pass

class sb(bank):
    def loan(self):
        print("u can get a loan upto 100000")
    def interst(self):
        print("interst at 1.25%")
b=sb()
b.interst()
b.loan()