with open("data.txt", "w") as f:
    f.write("Python is easy for beeginer")

with open("data.txt", "r") as f:
    text = f.read()

word_list = text.split()
print("Total words:", len(word_list))
