values = [10, 20, 30, 40, 50]

delete_num = int(input("Enter value to delete: "))

if delete_num in values:
    values.remove(delete_num)
    print("After deletion:", values)
else:
    print("Value not found")