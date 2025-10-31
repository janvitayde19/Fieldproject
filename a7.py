def print_odd_numbers(start, end):
    """
    Prints all odd numbers within a given range (inclusive).

    Args:
        start (int): The starting number of the range.
        end (int): The ending number of the range.
    """
    print(f"Odd numbers between {start} and {end}:")
    for number in range(start, end + 1):
        if number % 2 != 0:  # If the remainder when divided by 2 is not 0, it's odd
            print(number)

# Example usage:
minimum_value = 1
maximum_value = 20
print_odd_numbers(minimum_value, maximum_value)

# Another example using user input
try:
    user_start = int(input("Enter the starting number: "))
    user_end = int(input("Enter the ending number: "))
    if user_start <= user_end:
        print_odd_numbers(user_start, user_end)
    else:
        print("Starting number cannot be greater than the ending number.")
except ValueError:
    print("Invalid input. Please enter integers.")
