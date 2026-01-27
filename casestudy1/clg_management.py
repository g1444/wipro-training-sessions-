from abc import ABC, abstractmethod
import json, csv, os

# --------------------------decorators-----------------#

def log_exe(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper


def admin_only(func):
    def wrapper(*args, **kwargs):
        if not kwargs.get("is_admin", False):
            raise PermissionError("Access Denied: Admin privileges required")
        return func(*args, **kwargs)
    return wrapper


# ------------------descriptors------------------#

class SalaryDescriptor:
    def __get__(self, instance, owner):
        raise PermissionError("Access denied: salary is confidential")

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Salary must be positive")
        instance._salary = value


class MarksDescriptor:
    def __get__(self, instance, owner):
        return instance._marks

    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise ValueError("Marks must be a list")
        for m in value:
            if not isinstance(m, int) or not (0 <= m <= 100):
                raise ValueError("Marks must be between 0 and 100")
        instance._marks = value


# ----------------abstract person----------------#

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


# ----------------student----------------#

class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, id, name, dept, semester, marks=None):
        super().__init__(id, name, dept)
        self.semester = semester
        self.marks = marks if marks else []
        self.courses = []

    def calculate_performance(self):
        if not self.marks:
            return 0, "N/A"

        avg = sum(self.marks) / len(self.marks)
        if avg >= 90:
            grade = "A+"
        elif avg >= 80:
            grade = "A"
        elif avg >= 70:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        elif avg >= 50:
            grade = "D"
        else:
            grade = "F"

        return avg, grade

    def __gt__(self, other):
        return self.calculate_performance()[0] > other.calculate_performance()[0]

    def get_details(self):
        avg, grade = self.calculate_performance()
        return f"{self.id} | {self.name} | {self.dept} | {self.semester} | {avg:.2f} | {grade}"


# ----------------faculty----------------#

class Faculty(Person):
    salary = SalaryDescriptor()

    def __init__(self, id, name, dept, salary):
        super().__init__(id, name, dept)
        self.salary = salary

    def calculate_performance(self):
        return "Faculty performance based on feedback"

    def get_details(self):
        return f"{self.id} | {self.name} | {self.dept}"


# ----------------course----------------#

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


# ----------------department----------------#

class Department:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.faculty = []
        self.courses = []

    def add_student(self, student):
        if any(s.id == student.id for s in self.students):
            raise ValueError("Student ID already exists")
        self.students.append(student)

    def find_student(self, sid):
        return next((s for s in self.students if s.id == sid), None)

    def show_students_table(self):
        if not self.students:
            print("No students available")
            return

        print("\nID\tName\tDept\tSem\tAverage\tGrade")
        print("-" * 60)
        for s in self.students:
            avg, grade = s.calculate_performance()
            print(f"{s.id}\t{s.name}\t{s.dept}\t{s.semester}\t{avg:.2f}\t{grade}")


# ----------------file handling----------------#

def load_students_from_json(dept, filename="students.json"):
    if not os.path.exists(filename):
        return

    with open(filename, "r") as f:
        data = json.load(f)

    for s in data:
        student = Student(
            s["id"],
            s["name"],
            s["department"],
            s["semester"],
            s["marks"]
        )
        dept.students.append(student)

    print("Student data loaded from JSON")


@admin_only
def save_students_json(students, is_admin=False):
    data = []
    for s in students:
        avg, grade = s.calculate_performance()
        data.append({
            "id": s.id,
            "name": s.name,
            "department": s.dept,
            "semester": s.semester,
            "marks": s.marks,
            "average": avg,
            "grade": grade
        })

    with open("students.json", "w") as f:
        json.dump(data, f, indent=4)
    with open("student.csv","w",newline="") as f:
        writer=csv.writer(f)
        writer.writerow("id","name","Department","average","grade")
        for s in students:
            writer.writerow([s.id,s.name,s.dept,s.calulate_performance(),s.grade])
    print("Student data saved to JSON and csv files")


# ----------------main----------------#

def main():
    dept = Department("Computer Science")

    # ---------- auto load students ----------
    load_students_from_json(dept)

    role = input("Login as (admin/user): ").lower()
    is_admin = False

    if role == "admin":
        if input("Enter admin password: ") != "admin123":
            print("Invalid password")
            return
        is_admin = True
    elif role != "user":
        print("Invalid role")
        return

    while True:
        print("\n===== Smart University Management System =====")

        if is_admin:
            print("1. Add Student")
            print("2. Add Faculty")
            print("3. Add Course")
            print("4. Enroll Student to Course")
            print("5. Show Students (Table)")
            print("6. Compare Students")
            print("7. Save Data")
            print("8. Exit")

            choice = input("Enter choice: ")

            try:
                if choice == "1":
                    s = Student(
                        input("ID: "),
                        input("Name: "),
                        input("Department: "),
                        int(input("Semester: ")),
                        list(map(int, input("Marks: ").split()))
                    )
                    dept.add_student(s)
                    print("Student added")


                elif choice == "2":
                    f = Faculty(
                        input("ID: "),
                        input("Name: "),
                        input("Department: "),
                        int(input("Salary: "))
                    )
                    dept.faculty.append(f)
                    print("Faculty added")

                elif choice == "3":

                    if not dept.faculty:
                        print("No faculty available to assign")
                        continue

                    # 1️⃣ Get course details first
                    code = input("Course Code: ")
                    name = input("Course Name: ")
                    credits = int(input("Credits: "))

                    # 2️⃣ Show faculty list
                    print("\nAvailable Faculty:")
                    for f in dept.faculty:
                        print(f.id, "-", f.name)

                    # 3️⃣ Select faculty by ID
                    fid = input("Enter Faculty ID to assign: ")
                    fac = next((f for f in dept.faculty if f.id == fid), None)

                    if not fac:
                        print("Faculty not found")
                        continue

                    # 4️⃣ Create course
                    course = Course(code, name, credits, fac)
                    dept.courses.append(course)

                    print("Course added successfully")
                elif choice == "4":
                    sid = input("Student ID: ")
                    cid = input("Course Code: ")

                    stu = dept.find_student(sid)
                    crs = next((c for c in dept.courses if c.code == cid), None)

                    if not stu or not crs:
                        print("Student or Course not found")
                        continue

                    crs.enroll_student(stu)
                    print("Enrollment successful")

                elif choice == "5":
                    dept.show_students_table()

                elif choice == "6":
                    s1 = dept.find_student(input("First Student ID: "))
                    s2 = dept.find_student(input("Second Student ID: "))

                    if not s1 or not s2:
                        print("Student not found")
                        continue

                    print(s1.name, ">", s2.name, ":", s1 > s2)

                elif choice == "7":
                    save_students_json(dept.students, is_admin=True)

                elif choice == "8":
                    print("Exiting system")
                    break

                else:
                    print("Invalid choice")

            except Exception as e:
                print("Error:", e)

        else:
            # -------- USER MENU --------
            print("1. Show Students (Table)")
            print("2. Compare Students")
            print("3. Exit")

            choice = input("Enter choice: ")

            try:
                if choice == "1":
                    dept.show_students_table()

                elif choice == "2":
                    s1 = dept.find_student(input("First Student ID: "))
                    s2 = dept.find_student(input("Second Student ID: "))

                    if not s1 or not s2:
                        print("Student not found")
                        continue

                    print(s1.name, ">", s2.name, ":", s1 > s2)

                elif choice == "3":
                    print("Exiting system")
                    break

                else:
                    print("Invalid choice")

            except Exception as e:
                print("Error:", e)



main()