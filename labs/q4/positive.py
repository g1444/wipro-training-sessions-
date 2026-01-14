class positive_salary:
    def __get__(self,obj,objtype=None):
        return obj.__dict__.get("salary")
    def __set__(self,obj,value):
        if value<=0:
            raise ValueError("salary must be higher than 0")
        obj.__dict__["salary"]=value