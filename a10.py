numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break  # Exit the loop when num is 3
    print(num)

print("---")

for num in numbers:
    if num == 3:
        continue # Skip printing 3
    print(num)