with open("1.txt", "w") as f1:
    for i in range(1, 5):
        nm = input("Enter name: ")
        f1.write(nm)
        f1.write("\n")

with open("1.txt", "r") as f1:
    print(f1.read())

with open("1.txt", "a") as file:
    for i in range(1, 6):
        nm = input("Enter name: ")
        file.write(nm + "\n")

with open("1.txt", "r") as file:
    print(file.read())

with open("1.txt", "r") as file:
    nm = file.read()
    print("\n no of character in a file", len(nm))
    nm1 = nm.split()
    print("\n no of word in file", len(nm1))