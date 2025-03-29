# Fibonacci Sequence Generator
MAX_VALUE = 10000

def print_fibonacci():
    """Prints Fibonacci sequence terms up to MAX_VALUE."""
    a, b = 0, 1  # Initial Fibonacci numbers

    while a < MAX_VALUE:
        print(a, end=" ")  # Print the current term
        a, b = b, a + b  # Generate the next term

# Call the function
print_fibonacci()

