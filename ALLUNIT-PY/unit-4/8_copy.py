with open("data.txt", "w") as f:
    f.write("Hello!, welcome to python programming.")

with open("data.txt", "r") as f:
    content = f.read()

with open("backup.txt", "w") as f:
    f.write(content)

print("Data copied successfully")
