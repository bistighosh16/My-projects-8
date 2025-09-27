class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.courses = []
    def enroll(self, course):
        self.courses.append(course)
        course.students.append(self)
class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.courses = []
    def assign_course(self, course):
        self.courses.append(course)
        course.teacher = self
class Course:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.teacher = None
        self.students = []
class College:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.students = []
        self.teachers = []
    def add_course(self, course):
        self.courses.append(course)
    def add_student(self, student):
        self.students.append(student)
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
college = College("ABC Institute")
num_students = int(input("Enter number of students: "))
for _ in range(num_students):
    name = input("Student name: ")
    age = int(input("Student age: "))
    college.add_student(Student(name, age))
num_teachers = int(input("Enter number of teachers: "))
for _ in range(num_teachers):
    name = input("Teacher name: ")
    age = int(input("Teacher age: "))
    college.add_teacher(Teacher(name, age))
num_courses = int(input("Enter number of courses: "))
for _ in range(num_courses):
    name = input("Course name: ")
    code = input("Course code: ")
    college.add_course(Course(name, code))
for student in college.students:
    print(f"\nEnroll courses for {student.name}:")
    for i, course in enumerate(college.courses):
        print(f"{i+1}. {course.name}")
    choices = input("Enter course numbers separated by commas: ").split(",")
    for ch in choices:
        course_index = int(ch.strip()) - 1
        student.enroll(college.courses[course_index])
for course in college.courses:
    print(f"\nAssign teacher to course {course.name}:")
    for i, teacher in enumerate(college.teachers):
        print(f"{i+1}. {teacher.name}")
    choice = int(input("Enter teacher number: ")) - 1
    college.teachers[choice].assign_course(course)
print("\n--- College Data Summary ---")
for course in college.courses:
    print(f"\nCourse: {course.name} ({course.code})")
    print(f"Teacher: {course.teacher.name}")
    print("Students Enrolled:")
    for student in course.students:
        print(f" - {student.name}")
