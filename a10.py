while True:
    # Code to be executed at least once
    user_input = input("Enter 'quit' to exit: ")

    if user_input.lower() == 'quit':
        break  # Exit the loop if the condition is met

    print(f"You entered: {user_input}")

print("Loop finished.")