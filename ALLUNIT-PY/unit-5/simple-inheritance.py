class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)

class Student(Person):
    def show_course(self):
        print("Course: BCA")

S1 = Student("Yasir")
S1.show_name()
S1.show_course()
