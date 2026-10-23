try:
    num = int(input("Enter a number: "))

except ValueError:
    print("Please enter a valid number")

else:
    print("Qube:", num ** 3)

finally:
    print("Program completed")
