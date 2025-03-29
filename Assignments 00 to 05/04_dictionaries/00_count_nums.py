def get_user_numbers():
    """
    Prompts the user to enter numbers and stores them in a list.
    Stops when the user enters a blank line.
    """
    numbers = []
    while (num := input("Enter a number: ")):  # Read input using the walrus operator
        if num.isdigit():  # Check if input is a valid number
            numbers.append(int(num))  # Convert input to integer and store in list
        else:
            print("Invalid input. Please enter a number.")
    return numbers  # Return the list of numbers entered by the user


def count_nums(numbers):
    """
    Counts occurrences of each unique number in the list.
    Returns a dictionary with numbers as keys and their counts as values.
    """
    return {num: numbers.count(num) for num in set(numbers)}  # Use dictionary comprehension


def main():
    """
    Main function to handle user input, count occurrences, and display results.
    """
    numbers = get_user_numbers()  # Get numbers from the user
    counts = count_nums(numbers)  # Count occurrences of each number
    for num, count in counts.items():  # Iterate over the dictionary to print results
        print(f"{num} appears {count} times.")


if __name__ == "__main__":
    main()  # Run the main function
