class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Salary:", self.salary)

e1 = Employee("E001", "Yasir", 25000)
e2 = Employee("E002", "Hassan", 30000)
e1.display()
e2.display()
