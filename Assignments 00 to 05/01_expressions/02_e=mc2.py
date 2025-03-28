def calculate_energy(mass: float):
    c = 299792458  # Speed of light in m/s
    energy = mass * c**2  # Einstein's equation: E = mc²

    print("\ne = m * C^2...\n")
    print(f"m = {mass} kg")
    print(f"C = {c} m/s")
    print(f"{energy} joules of energy!\n")

if __name__ == '__main__':
    while True:
        user_input = input("Enter kilos of mass (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting program...")
            break
        try:
            mass = float(user_input)
            calculate_energy(mass)
        except ValueError:
            print("Invalid input! Please enter a valid number for mass.")
