"""Practice variables, common data types, and type conversion."""


def main():
    name = "Ranjay"
    age = 23
    height_m = 1.72
    is_learning = True

    print(f"{name} is {age} years old.")
    print(f"Height: {height_m} m; currently learning: {is_learning}")

    quantity = int("4")
    price = float("2.50")
    print("Total:", quantity * price)
    print("Types:", type(name).__name__, type(age).__name__,
          type(height_m).__name__, type(is_learning).__name__)


if __name__ == "__main__":
    main()
