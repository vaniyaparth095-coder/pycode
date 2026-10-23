name = input("Enter file name: ")

try:
    with open(name, "r") as f:
        data = f.read()
        print(data)

except FileNotFoundError:
    print("File not found")
