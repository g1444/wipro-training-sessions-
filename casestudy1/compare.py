from abc import ABC, abstractmethod
import json
import csv
import time

# ===================== DECORATORS =====================

def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Method {func.__name__}() started")
        result = func(*args, **kwargs)
        print(f"[LOG] Method {func.__name__}() executed successfully")
        return result
    return wrapper


def admin_only(func):
    def wrapper(*args, **kwargs):
        is_admin = kwargs.get("admin", False)
        if not is_admin:
            raise PermissionError("Access Denied: Admin privileges required")
        return func(*args, **kwargs)
    return wrapper


# ===================== DESCRIPTORS =====================

class MarksValidator:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance._marks

    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise ValueError("Marks must be a list")

        for m in value:
            if not isinstance(m, int) or not (0 <= m <= 100):
                raise ValueError("Marks should be between 0 and 100")

        instance._marks = value


class SalaryDescriptor:
    def __get__(self, instance, owner):
        raise PermissionError("Access Denied: Salary is confidential")

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Salary must be positive")
        instance._salary = value


# ===================== ABSTRACT BASE =====================

class Person(ABC):
    def __init__(self, id, name, dept):
        self.id = id
        self.name = name
        self.dept = dept

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def calculate_performance(self):
        pass


# ===================== STUDENT =====================

class Student(Person):
    marks = MarksValidator()

    def __init__(self, id, name, dept, semester, marks=None):
        super().__init__(id, name, dept)
        self.semester = semester
        self.marks = marks if marks else []
        self.courses = []

    def get_details(self):
        return f"Name: {self.name}\nRole: Student\nDepartment: {self.dept}"

    @log_execution
    def calculate_performance(self):
        if not self.marks:
            return 0
        avg = sum(self.marks) / len(self.marks)
        return avg

    def __gt__(self, other):
        return self.calculate_performance() > other.calculate_performance()


# ===================== FACULTY =====================

class Faculty(Person):
    salary = SalaryDescriptor()

    def __init__(self, id, name, dept, salary):
        super().__init__(id, name, dept)
        self.salary = salary
        self.courses = []

    def get_details(self):
        return f"Name: {self.name}\nRole: Faculty\nDepartment: {self.dept}"

    def calculate_performance(self):
        return "Faculty performance based on feedback"


# ===================== COURSE =====================

class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)
        student.courses.append(self)

    def __add__(self, other):
        return self.credits + other.credits

    def __iter__(self):
        return iter(self.students)


# ===================== DEPARTMENT =====================

class Department:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.faculty = []
        self.courses = []

    def add_student(self, student):
        if any(s.id == student.id for s in self.students):
            raise ValueError("Error: Student ID already exists")
        self.students.append(student)

    def add_faculty(self, faculty):
        self.faculty.append(faculty)

    def add_course(self, course):
        self.courses.append(course)

    def student_generator(self):
        for s in self.students:
            yield s


# ===================== FILE HANDLING =====================

def save_students_json(students, filename="students.json"):
    data = []
    for s in students:
        data.append({
            "id": s.id,
            "name": s.name,
            "department": s.dept,
            "average": s.calculate_performance()
        })
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print("Student data successfully saved to students.json")


def generate_csv_report(students, filename="students_report.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Department", "Average"])
        for s in students:
            writer.writerow([s.id, s.name, s.dept, s.calculate_performance()])
    print("CSV Report generated")


# ===================== DEMO =====================

if __name__ == "__main__":
    cs = Department("Computer Science")

    s1 = Student("S101", "Ananya Sharma", "Computer Science", 4, [78, 85, 90, 88, 92])
    s2 = Student("S102", "Rohan Verma", "Computer Science", 4, [60, 70, 75, 80, 85])

    f1 = Faculty("F201", "Dr. Rajesh Kumar", "Computer Science", 85000)

    c1 = Course("CS401", "Data Structures", 4, f1)
    c2 = Course("CS402", "Algorithms", 3, f1)

    cs.add_student(s1)
    cs.add_student(s2)
    cs.add_faculty(f1)
    cs.add_course(c1)
    cs.add_course(c2)

    c1.enroll_student(s1)
    c2.enroll_student(s1)

    print("\n--- Student Performance ---")
    print(s1.calculate_performance())

    print("\n--- Polymorphism Demo ---")
    print(s1.get_details())
    print(f1.get_details())

    print("\n--- Operator Overloading ---")
    print("Credits after merge:", c1 + c2)
    print("Ananya > Rohan :", s1 > s2)

    print("\n--- Generator Demo ---")
    for student in cs.student_generator():
        print(student.id, student.name)

    save_students_json(cs.students)
    generate_csv_report(cs.students)
