product = []

def add():
    pid = int(input("Enter PID: "))
    pname = input("Enter Product name: ")
    price = int(input("Enter Product Price: "))

    d1 = {"PID": pid, "PName": pname, "Price": price}
    product.append(d1)
    print("Product added successfully!")

def display():
    if not product:
        print("No products available.")
        return

    print("===================================")
    print("Product ID   Product Name   Price")
    print("===================================")

    for p1 in product:
        print(p1["PID"], "          ", p1["PName"], "       ", p1["Price"])

def search():
    pid = int(input("Enter PID: "))

    for p1 in product:
        if p1["PID"] == pid:
            print("Product is found")
            print("Product ID:", p1["PID"])
            print("Product Name:", p1["PName"])
            print("Product Price:", p1["Price"])
            return

    print("Product not found")

def updateName():
    pid = int(input("Enter PID whose name you want to change: "))

    for p1 in product:
        if p1["PID"] == pid:
            pname = input("Enter new Product name: ")
            p1["PName"] = pname
            print("Product name updated successfully!")
            return

    print("Product not found")

def deletebyPID():
    pid = int(input("Enter PID you want to delete: "))

    for p1 in product:
        if p1["PID"] == pid:
            product.remove(p1)
            print("Product deleted successfully!")
            return

    print("Product not found")

def sortByPrice():
    if not product:
        print("No products available to sort.")
        return

    product.sort(key=lambda x: x["Price"])
    print("Products sorted by price successfully!")
    display()

while True:
    print("\n===== PRODUCT MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. Display Products")
    print("3. Search Product")
    print("4. Update Product Name")
    print("5. Delete Product")
    print("6. Sort Products by Price")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add()
    elif choice == "2":
        display()
    elif choice == "3":
        search()
    elif choice == "4":
        updateName()
    elif choice == "5":
        deletebyPID()
    elif choice == "6":
        sortByPrice()
    elif choice == "7":
        print("Thank you!")
        break
    else:
        print("Invalid choice! Please try again.")