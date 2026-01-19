class box:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return box(self.value+ other.value)
b1=box(23)
b2=box(34)
print((b1+b2))