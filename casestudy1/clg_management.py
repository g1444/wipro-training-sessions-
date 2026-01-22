from abc import ABC,abstractmethod
# login wrapper
def log_exe(func):
    def wrapper(*args,**kwargs):
        print(f"[log] methond {func.__name__}() started")
        result=func(*args,**kwargs)
        print(f"[log] method {func.__name__}() executed successfully")
        return result
    return wrapper
#  confirmaing salary confidentiality and ensuring salary is positive
class salarydes:
    def __get__(self,instance,owner):
        raise PermissionError("Access denied : salary is confidential")
    def __set__(self,instance,value):
        if value<=0:
            return ValueError("salary must be positive")
        instance._salary=value

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

# confirming the marks are between 0 to 100
class aremarks:
    def __get__(self,instance,owner):
        if instance is None:
            return self
        
        return instance._marks
    def __set__(self,instance,value):
        if not isinstance(value,list):
            return ValueError("Marks must be ina list")
        for m in value:
            if not isinstance(value,int) or not (0<=m<=100):
                raise ValueError("marks must be whole numbers")
        instance._marks=value
# -------------------student------------------#
class student(person):
    marks=aremarks()
    def __init__(self,id,name,dept,semester,marks=None,courses=None):
        super().__init__(id,name,dept)
        self.semester=semester
        self.marks=marks if marks else []
        self.courses=courses if courses else []
    def get_details(self):
        return f"name: {self.name}\nrole : student\ndepartment:{self.dept}"
    @log_exe
    def calculate_performance(self):
        if not self.marks:
            return 0
        avg=sum(self.marks)/len(self.marks)
        return avg
    def __gt__(self,other):
        return self.calculate_performance()>other.calsulate_performance()
# -----------------------student--------------------#
class faculty(person):
    salary=salarydes()
    def __init__(self, id, name, dept,salary,courses):
        super().__init__(id, name, dept)
        self.salary=salary
        self.courses=[]
    def get_details(self):
        return f'Name: {self.name}\nRole: Faculty\ndepartment: {self.dept}'
    def calculate_performance(self):
        return "Faculty performance based on feedback"
# -----------------faculty-------------#
# ------------course-----------#
class courses:
    def __init__(self,code,name,credits,faculty):
        self.code=code
        self.name=name
        self.credits=credits
        self.facultyu=faculty
        self.students=[]
    def enroll_students(self,student):
        self.students.append(student)
        student.courses.append(self)
# ---------course----------------#

#  -------------department class----------#

class department:
    def _init__(self,name):
        self.name=name
        self.faculty=[]
        self.courses=[]