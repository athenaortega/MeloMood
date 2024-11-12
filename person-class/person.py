class Person:
    def __init__(self, name):
        self.name = name


class Teacher(Person):
    def __init__(self, name, courses_taught):
        super().__init__(name)
        self.courses_taught = []

        def add_course(self, course_name):
            self.courses_taught.append(course_name)



class Student(Person):
    def __init__(self, name, courses_enrolled):
        super().__init__(name)
        self.courses_enrolled = []



class Course():
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
        self.teacher.add_student(self)