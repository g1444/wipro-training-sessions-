from abc import ABC,abstractmethod
class person(ABC):
    def __init__(self,id,name,dept):
        self.id=id
        self.name=name
        self.dept=dept
    @abstractmethod
    def get_details(self):
        pass
    def calculate_performance(self):
        pass
class aremarks:
    def __get__(self,instance,owner):
        
        return instance.__dict__("marks")
    def __set__(self,instance,value):
        if not isinstance(value,int) or value<0:
            raise ValueError("marks must be whole numbers")
        instance.__dict__("marks")=value

class student(person):
    marks=aremarks()
    def __init__(self,id,name,dept,semester,marks=None,courses=None):
        super().__init__(id,name,dept)
        self.semester=semester
        self.marks=marks if marks else []
        self.enrolled_courses=courses if courses else []

