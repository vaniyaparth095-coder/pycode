class Employee:
    # --- STEP 1: The Constructor (__init__) ---
    def __init__(self, e_id, e_name):
        self.e_id = e_id          # Employee ID
        self.e_name = e_name      # Employee Name
        self.bs = 0               # Basic Salary
        self.hra = 0              # House Rent Allowance
        self.da = 0               # Dearness Allowance
        self.pf = 0               # Provident Fund
        self.ns = 0               # Net Salary
        
    # --- STEP 2: Input Method ---
    def get_data(self):
        # Basic Salary must be converted to an integer/float for calculations
        self.bs = int(input("Enter Basic Salary: "))
        
    # --- STEP 3: Salary Calculation Logic ---
    def calculate(self):
        # HRA Calculation based on Basic Salary thresholds
        if self.bs >= 30000:
            self.hra = self.bs * 0.30
        else:
            self.hra = self.bs * 0.15
            
        # DA and PF Calculations
        self.da = self.bs * 0.20
        self.pf = self.bs * 0.12
        
        # Net Salary Formula
        self.ns = (self.bs + self.hra + self.da) - self.pf
        
    # --- STEP 4: Display Method ---
    def put_data(self):
        print(f"Employee Id   : {self.e_id}")
        print(f"Employee Name : {self.e_name}")
        print(f"Basic Salary  : {self.bs}")
        print(f"HRA is        : {self.hra}")
        print(f"DA is         : {self.da}")
        print(f"PF deduction  : {self.pf}")
        print(f"Net Salary is : {self.ns}")
        print("-" * 30)

# --- STEP 5: Main Program Execution ---
emp = []  # List to store employee objects

# Loop to create and process 3 employees
for i in range(1, 4):
    print(f"\n--- Entering details for Employee {i} ---")
    name = input("Enter Name: ")
    
    # Create object instance (passing i as e_id)
    e1 = Employee(i, name)
    
    # Call methods sequentially
    e1.get_data()
    e1.calculate()
    
    # Append the object instance to our list
    emp.append(e1)

# Loop to display all stored records
print("\n================ EMPLOYEE DETAILS ================")
for i in range(3):
    emp[i].put_data()