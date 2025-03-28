import random  # Importing the random module to generate random numbers

# Define the number of sides on each die
num : int = 6

def main():
    """
    Simulates rolling two dice and prints the result of each die
    as well as their total.
    """
    
    # Roll the dice by generating random numbers between 1 and NUM_SIDES
    die1: int = random.randint(1, num)
    die2: int = random.randint(1, num)
    
    # Calculate the total
    total: int = die1 + die2
    
    # Print the results
    print(f"Dice have {num} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")


if __name__ == '__main__':
    main()
