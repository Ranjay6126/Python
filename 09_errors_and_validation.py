"""Practice handling expected errors and validating values."""


def parse_positive_integer(text):
    try:
        number = int(text)
    except ValueError:
        return None
    return number if number > 0 else None


def main():
    for value in ("12", "hello", "-3"):
        number = parse_positive_integer(value)
        if number is None:
            print(f"{value!r} is not a positive whole number.")
        else:
            print(f"Accepted: {number}")

    values = [10, 0, 5]
    try:
        print("Average:", sum(values) / len(values))
    except ZeroDivisionError:
        print("Cannot calculate the average of an empty list.")


if __name__ == "__main__":
    main()
