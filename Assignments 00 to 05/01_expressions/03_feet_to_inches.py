def convert_feet_to_inches(feet: float) -> float:
    inches = feet * 12  # 1 foot = 12 inches
    return inches

def main():
    while True:
        user_input = input("Enter length in feet (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting program...")
            break
        try:
            feet = float(user_input)
            inches = convert_feet_to_inches(feet)
            print(f"{feet} feet is equal to {inches} inches.\n")
        except ValueError:
            print("Invalid input! Please enter a valid number for feet.")

if __name__ == '__main__':
    main()
