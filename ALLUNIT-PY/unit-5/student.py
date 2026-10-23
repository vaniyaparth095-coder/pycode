class Student:
    def display(self):
        print("Name:", self.name)
        print("Roll number:", self.roll_number)
        print("Age:",self.age)

s1 = Student()
s1.name = "Yasir"
s1.roll_number = 25
s1.age = 18
s1.display()
