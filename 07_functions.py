"""Practice reusable functions, defaults, and return values."""


def calculate_total(prices, tax_rate=0.0):
    """Return the sum of prices with tax applied."""
    subtotal = sum(prices)
    return subtotal * (1 + tax_rate)


def describe_person(name, age):
    return f"{name.title()} is {age} years old."


def main():
    total = calculate_total([12.50, 7.25], tax_rate=0.08)
    print(f"Total with tax: ${total:.2f}")
    print(describe_person("sam", 28))


if __name__ == "__main__":
    main()
