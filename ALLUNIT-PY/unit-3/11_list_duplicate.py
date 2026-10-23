values = [2, 4, 2, 6, 4, 8, 2]
unique_values = []

for num in values:
    if num not in unique_values:
        unique_values.append(num)

print("Without duplicates:", unique_values)