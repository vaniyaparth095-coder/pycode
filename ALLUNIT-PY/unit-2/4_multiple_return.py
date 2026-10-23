def math_operations(num1, num2):
    return num1 + num2, num1 - num2, num1 * num2

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

add_result, sub_result, mul_result = math_operations(first, second)

print("Addition =", add_result)
print("Subtraction =", sub_result)
print("Multiplication =", mul_result)