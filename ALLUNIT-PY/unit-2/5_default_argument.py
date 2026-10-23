def find_power(num, power=2):
    return num ** power

n = int(input("Enter a number: "))

print("Square =", find_power(n))
print("Cube =", find_power(n, 3))