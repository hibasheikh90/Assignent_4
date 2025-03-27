MINIMUM_HEIGHT = 50  # Minimum height in arbitrary units

def main():
    height = float(input("How tall are you? "))  # Take input and convert to float
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    main()
