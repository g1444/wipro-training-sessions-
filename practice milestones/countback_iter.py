class Iterator_backwards:
    def __iter__(self,y):
        self.n=y
        return self
    def __next__(self):
        x=self.n
        self.n-=1
        return x
b=Iterator_backwards()
p=b.__iter__(10)
print(next(p))
print(next(p))