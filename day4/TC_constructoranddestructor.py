class employee:
    def __init__(self,name):
        self.name=name
        print("name:",name)
    def __del__(self):
        print("deleted")
e=employee("dinesh")