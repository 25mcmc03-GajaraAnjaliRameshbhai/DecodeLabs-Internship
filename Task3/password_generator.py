# ==================================
# DecodeLabs Project 3
# Random Password Generator
# ==================================

import secrets
import string


def is_valid_password(password):
    """Check whether the password satisfies all required constraints."""

    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    return (
        has_uppercase
        and has_lowercase
        and has_digit
        and has_special
    )


def generate_password(length):
    """Generate a secure password with all required character types."""

    # Add at least one character from each required category
    password_chars = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    # Character pool for the remaining password
    all_characters = (
        string.ascii_uppercase
        + string.ascii_lowercase
        + string.digits
        + string.punctuation
    )

    # Generate remaining characters
    for _ in range(length - 4):
        password_chars.append(secrets.choice(all_characters))

    # Securely shuffle the password
    secrets.SystemRandom().shuffle(password_chars)

    password = ''.join(password_chars)

    return password


print("=" * 50)
print("          RANDOM PASSWORD GENERATOR")
print("=" * 50)

print("\nPassword Requirements:")
print("• Minimum 8 characters")
print("• At least one uppercase letter (A-Z)")
print("• At least one lowercase letter (a-z)")
print("• At least one digit (0-9)")
print("• At least one special character (!, @, #, $, etc.)")


while True:

    try:
        length = int(input("\nEnter password length (8-64): "))

        if length < 8:
            print("Password must be at least 8 characters long.")
            continue

        if length > 64:
            print("Password length cannot exceed 64 characters.")
            continue

        password = generate_password(length)

        # Verify generated password
        if is_valid_password(password):

            print("\n" + "=" * 50)
            print("Generated Password:")
            print(password)
            print("=" * 50)

            print("\nPassword Validation:")
            print("✓ Uppercase letter included")
            print("✓ Lowercase letter included")
            print("✓ Digit included")
            print("✓ Special character included")
            print(f"✓ Password length: {len(password)}")

            break

        else:
            print("Password generation failed. Trying again...")

    except ValueError:
        print("Invalid input! Please enter a whole number.")


print("\nPassword generated successfully!")
