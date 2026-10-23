import CrudOp as c1

while True:
    print("\n*** PRODUCT MANAGEMENT SYSTEM ***")
    print("1. Add Product")
    print("2. Display")
    print("3. Update")
    print("4. Delete")
    print("5. Search")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")
    print("---------------------------------")

    if choice == "1":
        c1.add()
    elif choice == "2":
        c1.display()
    elif choice == "3":
        c1.updateName()
    elif choice == "4":
        c1.deletebyPID()
    elif choice == "5":
        c1.search()
    elif choice == "6":
        print("Exiting application. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")