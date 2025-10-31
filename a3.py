# Get input from the user for the first number
num1_str = input("Enter the first number: ")

# Get input from the user for the second number
num2_str = input("Enter the second number: ")

try:
    # Convert the input strings to floating-point numbers
    num1 = float(num1_str)
    num2 = float(num2_str)

    # Perform addition
    addition_result = num1 + num2

    # Perform multiplication
    multiplication_result = num1 * num2

    # Print the results
    print(f"The sum of {num1} and {num2} is: {addition_result}")
    print(f"The product of {num1} and {num2} is: {multiplication_result}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")