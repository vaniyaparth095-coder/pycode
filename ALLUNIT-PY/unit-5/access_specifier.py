class Student:
    # --- STEP 1: Constructor to initialize private attributes ---
    def __init__(self):
        # Double underscores '__' make these variables private
        self.__rno = int(input("Enter roll number: "))
        self.__name = input("Enter name: ")
        self.__mks = float(input("Enter marks: "))

    # --- STEP 2: Public method to safely display the private data ---
    def put_data(self):
        print("\n--- Student Details ---")
        print("Roll No is :", self.__rno)
        print("Name is    :", self.__name)
        print("Marks is   :", self.__mks)


# --- MAIN PROGRAM EXECUTION ---
# 1. Create an object of the Student class (triggers __init__)
S1 = Student()

# 2. Display the data using the authorized public method
S1.put_data()

# 3. Demonstrating Private Member Behavior (as noted in your diary):
# Trying to change the private member directly outside the class will NOT work as expected.
# Instead of modifying the internal __rno, Python creates a separate public variable.
S1.__rno = 76  
S1.__name = "abc"

print("\nAttempted to change private variables directly from outside...")

# 4. Verifying that the internal private variables remain safe and unchanged:
S1.put_data()