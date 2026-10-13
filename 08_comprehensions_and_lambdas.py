"""Practice comprehensions, lambda functions, and custom sorting."""


def main():
    numbers = range(1, 11)
    squares = [number**2 for number in numbers]
    even_squares = [square for square in squares if square % 2 == 0]
    print("Squares:", squares)
    print("Even squares:", even_squares)

    people = [("Mina", 31), ("Arun", 24), ("Lee", 28)]
    youngest_first = sorted(people, key=lambda person: person[1])
    print("Sorted by age:", youngest_first)

    word_lengths = {word: len(word) for word in ("python", "code", "practice")}
    print("Word lengths:", word_lengths)


if __name__ == "__main__":
    main()
