class a:
    def showA(self):
        print("a")
class b(a):
    def showB(self):
        print("b")

class c(b):
    pass
c=c()
c.showA()
c.showB()

