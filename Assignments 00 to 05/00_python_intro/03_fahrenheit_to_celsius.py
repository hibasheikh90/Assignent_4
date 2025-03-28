def main():
    # Prompting the user to enter temperature in Fahrenheit
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Converting Fahrenheit to Celsius
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

    # Displaying the result
    print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")

# Calling the main function
if __name__ == '__main__':
    main()
