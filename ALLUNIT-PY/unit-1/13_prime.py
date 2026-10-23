number = int(input("Enter a number: "))
check = 0

if number < 2:
    check = 1
else:
    for divisor in range(2, number):
        if number % divisor == 0:
            check = 1
            break

if check == 0:
    print("Prime number")
else:
    print("Not a prime number")