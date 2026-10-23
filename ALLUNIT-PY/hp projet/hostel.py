students = []

def add_student():
    sid = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    room = input("Enter Room Number: ")
    fees = int(input("Enter Hostel Fees: "))

    student = {
        "ID": sid,
        "Name": name,
        "Age": age,
        "Room": room,
        "Fees": fees
    }

    students.append(student)
    print("Student added successfully!")

def display_students():
    if not students:
        print("No student records found.")
        return

    print("\nID   Name   Age   Room   Fees")
    print("--------------------------------")

    for s in students:
        print(s["ID"], s["Name"], s["Age"],
              s["Room"], s["Fees"])

def search_student():
    sid = int(input("Enter Student ID to search: "))

    for s in students:
        if s["ID"] == sid:
            print("Student Found!")
            print("ID:", s["ID"])
            print("Name:", s["Name"])
            print("Age:", s["Age"])
            print("Room:", s["Room"])
            print("Fees:", s["Fees"])
            return

    print("Student not found.")

def update_student():
    sid = int(input("Enter Student ID to update: "))

    for s in students:
        if s["ID"] == sid:
            s["Name"] = input("Enter New Name: ")
            s["Age"] = int(input("Enter New Age: "))
            s["Room"] = input("Enter New Room Number: ")
            print("Student updated successfully!")
            return

    print("Student not found.")

def delete_student():
    sid = int(input("Enter Student ID to delete: "))

    for s in students:
        if s["ID"] == sid:
            students.remove(s)
            print("Student deleted successfully!")
            return

    print("Student not found.")

def allocate_room():
    sid = int(input("Enter Student ID: "))

    for s in students:
        if s["ID"] == sid:
            s["Room"] = input("Enter Room Number: ")
            print("Room allocated successfully!")
            return

    print("Student not found.")

def pay_fees():
    sid = int(input("Enter Student ID: "))

    for s in students:
        if s["ID"] == sid:
            amount = int(input("Enter Fee Amount Paid: "))
            s["Fees"] = max(0, s["Fees"] - amount)
            print("Remaining Fees:", s["Fees"])
            return

    print("Student not found.")

while True:
    print("\n===== HOSTEL MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Allocate Room")
    print("7. Pay Fees")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        allocate_room()
    elif choice == "7":
        pay_fees()
    elif choice == "8":
        print("Thank you for using Hostel Management System!")
        break
    else:
        print("Invalid choice! Please try again.")
