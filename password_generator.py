import random
import string

def generate_password(length, use_uppercase, use_digits, use_special):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return None  # Invalid case: No character types selected

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_boolean_input(prompt):
    while True:
        choice = input(prompt).lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        else:
            print("Invalid input! Enter 'y' or 'n'.")

# --- User Interaction ---
print("=== Secure Password Generator ===")
try:
    length = int(input("Enter password length (minimum 4): "))
    if length < 4:
        print("Error: Password length must be at least 4.")
    else:
        use_uppercase = get_boolean_input("Include uppercase letters? (y/n): ")
        use_digits = get_boolean_input("Include digits? (y/n): ")
        use_special = get_boolean_input("Include special characters? (y/n): ")

        password = generate_password(length, use_uppercase, use_digits, use_special)

        if password:
            print(f"Generated password: {password}")
        else:
            print("Error: You must select at least one character type!")
except ValueError:
    print("Error: Please enter a valid number for password length.")
