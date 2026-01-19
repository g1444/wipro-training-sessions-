class parent:
    def p1(self):
        print("parent")
class child1(parent):
    def c1(self):
        print("child1")
class child2(parent):
    def c2(self):
        print("child2")
C1=child1()
C1.p1()
C1.c1()
C2=child2()
C2.p1()
C2.c2()