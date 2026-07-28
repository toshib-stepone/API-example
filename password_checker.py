import re


def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add a number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add a special character.")

    levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    strength = levels[score - 1] if score > 0 else "Very Weak"

    return strength, feedback


def main():
    password = input("Enter a password to check: ")
    strength, feedback = check_password_strength(password)

    print(f"\nStrength: {strength}")
    if feedback:
        print("Suggestions:")
        for tip in feedback:
            print(f"- {tip}")
    else:
        print("Great password!")


if __name__ == "__main__":
    main()