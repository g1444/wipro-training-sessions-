# for x in [12,2,4,5]:
    # print(x)

class count:
    def __init__(self,limit):
        self.limit=limit
        self.current=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<self.limit:
            val=self.current
            self.current+=1
            return val
        else:
            raise StopIteration
obj=count(3)
for i in obj:
    print(i)