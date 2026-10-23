# --- STEP 1: Parent / Base Class ---
class Student:
    def __init__(self):
        # Input standard student demographics
        self.rno = int(input("Enter Roll No: "))
        self.nm = input("Enter Name: ")
        self.age = int(input("Enter Age: "))

    def put_data(self):
        print("\n--- Student Details ---")
        print("Roll No :", self.rno)
        print("Name    :", self.nm)
        print("Age     :", self.age)


# --- STEP 2: Child / Derived Class inheriting from Student ---
class Result(Student):
    def __init__(self):
        # Call the parent class constructor to set up rno, nm, and age
        super().__init__()
        
        # Initialize child-specific properties
        self.m1 = int(input("Enter Marks 1: "))
        self.m2 = int(input("Enter Marks 2: "))
        self.tot = 0
        self.per = 0.0

    def calculate(self):
        # Compute results
        self.tot = self.m1 + self.m2
        self.per = self.tot / 2.0

    def put_result(self):
        # First call parent's display method to avoid code repetition
        self.put_data()
        
        # Display child-specific metrics
        print("Marks 1 :", self.m1)
        print("Marks 2 :", self.m2)
        print("Total   :", self.tot)
        print("Percentage:", self.per, "%")


# --- MAIN PROGRAM EXECUTION ---
# Instantiate the child class object
R1 = Result()

# Run the calculation engine
R1.calculate()

# Display all aggregated metrics
print("\n================ FINAL REPORT ================")
R1.put_result()