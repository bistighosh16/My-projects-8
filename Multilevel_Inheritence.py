class School:
    def __init__(self, name):
        self.name = name
    def display_school(self):
        print(f"School Name: {self.name}")
class Course(School):
    def __init__(self, school_name, course_name):
        super().__init__(school_name)
        self.course_name = course_name
    def display_course(self):
        print(f"Course Name: {self.course_name}")
class Teacher(Course):
    def __init__(self, school_name, course_name, teacher_name):
        super().__init__(school_name, course_name)
        self.teacher_name = teacher_name
    def display_teacher(self):
        print(f"Teacher: {self.teacher_name}")
class Student(Teacher):
    def __init__(self, school_name, course_name, teacher_name, student_name):
        super().__init__(school_name, course_name, teacher_name)
        self.student_name = student_name
    def display_student(self):
        print(f"Student: {self.student_name}")
student = Student("ABC High School", "Mathematics", "Mr. Sen", "Aishi")
student.display_school()
student.display_course()
student.display_teacher()
student.display_student()
