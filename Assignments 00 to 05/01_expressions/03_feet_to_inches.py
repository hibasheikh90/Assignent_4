# This program converts feet to inches.
def main():
    feet = float(input("Enter feet: "))  # Get input from user
    inches = feet * 12  # Convert to inches
    print(f"{feet} feet = {inches} inches")  # Print result

if __name__ == '__main__':
    main()
