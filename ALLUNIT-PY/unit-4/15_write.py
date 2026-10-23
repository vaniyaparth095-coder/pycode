data = input("Enter some text: ")

with open("data.txt", "w") as f:
    f.write(data)

print("Data saved successfully")
