try:
    a = int(input("Enter number first: "))
    b = int(input("Enter number second: "))

    ans = a / b
    print("Answer:", ans)

except ZeroDivisionError:
    print("Division by zero is not possible")

except ValueError:
    print("enter a valid integer")
