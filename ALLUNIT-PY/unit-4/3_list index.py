data = [5, 15, 25, 35, 45]

try:
    pos = int(input("Enter index from 0 to 4: "))
    print("Element:", data[pos])

except IndexError:
    print("Invalid index")

except ValueError:
    print("Please enter a valid integer")
