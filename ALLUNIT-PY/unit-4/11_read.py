with open("students.txt", "w") as file:
    file.write("Name: Hassan\nCourse: BSc IT\n")

with open("students.txt", "r") as file:
    data = file.read()
    print(data)
