n = int(input("Enter a number: "))
fact = 1

if n < 0:
    print("Factorial is not possible")
else:
    for i in range(1, n + 1):
        fact = fact * i
    print("Factorial =", fact)