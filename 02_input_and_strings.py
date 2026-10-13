"""Practice input, useful string methods, and formatted strings."""


def main():
    name = input("What is your name? ").strip()
    city = input("What city do you live in? ").strip()

    if not name or not city:
        print("Please enter a name and a city next time.")
        return

    print(f"Hello, {name.title()}! You live in {city.title()}.")
    print("Your name has", len(name), "characters.")
    print("Uppercase:", name.upper())


if __name__ == "__main__":
    main()
