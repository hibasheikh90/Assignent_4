# This script implements a simple phonebook using a dictionary in Python.
# It allows users to add contacts with names and phone numbers, view all contacts,

def main():
    phonebook = {}  # Dictionary to store names and phone numbers
    
    while True:
        action = input("Enter 'add' to add a contact, 'view' to see contacts, or 'exit' to quit: ").lower()
        
        if action == 'add':
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            phonebook[name] = number  # Store name-number pair in dictionary
            print(f"Contact {name} added.")
        
        elif action == 'view':
            if phonebook:
                for name, number in phonebook.items():
                    print(f"{name}: {number}")
            else:
                print("Phonebook is empty.")
        
        elif action == 'exit':
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Try again.")

if __name__ == '__main__':
    main()
