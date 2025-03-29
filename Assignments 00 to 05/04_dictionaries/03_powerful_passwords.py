# Powerful Passwords with SHA256 Hashing
# This script demonstrates how to securely store and verify passwords using SHA256 hashing.


from hashlib import sha256  # Import SHA256 hashing function

def hash_password(password):
    """Returns the SHA256 hash of the given password."""
    return sha256(password.encode()).hexdigest()

def login(email, stored_logins, password):
    """Checks if the hashed password matches the stored hash for the given email."""
    return stored_logins.get(email) == hash_password(password)

def main():
    """Stores hashed passwords and verifies login attempts."""
    stored_logins = {
        "user@example.com": hash_password("mypassword123"),
        "test@website.com": hash_password("securepass"),
        "admin@secure.com": hash_password("admin123")
    }

    # Example login attempts
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if login(email, stored_logins, password):  # Pass stored_logins correctly
        print("Login successful!")
    else:
        print("Invalid email or password.")

if __name__ == '__main__':
    main()
