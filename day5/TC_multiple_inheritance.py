class a:
    def showA(self):
        print("a")
class b:
    def showA(self):
        print("a from b")
    def showB(self):
        print("b")

class c(a,b):
    pass

class d(b,a):
    pass
c=c()
d=d()
c.showA()
c.showB()
d.showB()
d.showA()
