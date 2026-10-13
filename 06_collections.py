"""Practice lists, tuples, sets, and dictionaries."""


def main():
    fruits = ["apple", "banana", "apple"]
    fruits.append("orange")
    print("List:", fruits)
    print("First fruit:", fruits[0])

    coordinates = (12, 8)
    print("Tuple coordinates:", coordinates)

    unique_fruits = set(fruits)
    print("Unique fruits:", sorted(unique_fruits))

    inventory = {"apples": 4, "bananas": 2}
    inventory["oranges"] = 3
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")


if __name__ == "__main__":
    main()
