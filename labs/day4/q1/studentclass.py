class student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def display_info(self):
        print(self.name,self.roll_no)

s1=student("gowtham",190)
s2=student("varsha",191)

s1.display_info()
s2.display_info()