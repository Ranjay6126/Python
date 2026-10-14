"""Practice using regular expressions to validate input."""

import re


def main():
    text = "Contact me at john.doe@example.com or support@company.org"
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    print("Emails found:", emails)

    phone_numbers = ["+91 98765 43210", "9876543210", "123-456-7890"]
    pattern = r"^\+?\d{10,13}$|^\+?\d{3}-\d{3}-\d{4}$"

    for number in phone_numbers:
        if re.match(pattern, number.replace(" ", "")):
            print(f"{number} is valid")
        else:
            print(f"{number} is invalid")

    name = "Ranjay6126"
    if re.fullmatch(r"[A-Za-z]+\d+", name):
        print(f"{name} matches the pattern")
    else:
        print(f"{name} does not match the pattern")


if __name__ == "__main__":
    main()
