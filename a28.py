items = ["apple", "banana", "orange", "grape"]
num_iterations = 10

print("Cycling through items:")
for i in range(num_iterations):
    index = i % len(items)
    print(items[index])