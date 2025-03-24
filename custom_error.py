user_input = input("Enter the number between 2 & 5 (or type 'quit' to exit): ")

if user_input.lower() == "quit":
    print("quit")  # Just print "quit" and continue execution
else:
    try:
        a = int(user_input)  # Convert input to integer

        if a < 2 or a > 5:
            raise ValueError("The number should be between 2 and 5")

        print(f"Valid number entered: {a}")

    except ValueError as e:
        print(f"Invalid input: {e}")  # Handle invalid numbers or non-numeric input
