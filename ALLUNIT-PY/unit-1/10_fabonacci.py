terms = int(input("Enter number of terms: "))
first = 0
second = 1

for count in range(terms):
    print(first, end=" ")
    next_num = first + second
    first = second
    second = next_num

print()