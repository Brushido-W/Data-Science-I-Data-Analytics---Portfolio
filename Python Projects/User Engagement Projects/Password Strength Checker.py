import re

def check_password_strength(password):
    """
    Checks the strength of a password.

    Args:
        password (str): The password to check.

    Returns:
        str: The strength of the password ('Weak', 'Moderate', 'Strong', or 'Very Strong').
    """
    # Calculate password length
    length = len(password)

    # Check if password contains uppercase letters
    has_uppercase = re.search(r"[A-Z]", password) is not None

    # Check if password contains lowercase letters
    has_lowercase = re.search(r"[a-z]", password) is not None

    # Check if password contains digits
    has_digits = re.search(r"\d", password) is not None

    # Check if password contains special characters
    has_special_chars = re.search(r"\W", password) is not None

    # Evaluate password strength based on criteria
    if length < 8 or not has_uppercase or not has_lowercase or not has_digits or not has_special_chars:
        return "Weak"
    elif length < 10 or not has_special_chars:
        return "Moderate"
    elif length < 12:
        return "Strong"
    else:
        return "Very Strong"


# Test the password strength checker
password = input("Enter a password: ")
strength = check_password_strength(password)
print("Password Strength:", strength)
