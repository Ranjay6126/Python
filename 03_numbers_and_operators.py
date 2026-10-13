"""Practice arithmetic, comparisons, and boolean operators."""


def main():
    first = 17
    second = 5

    print("Addition:", first + second)
    print("Division:", first / second)
    print("Whole-number division:", first // second)
    print("Remainder:", first % second)
    print("Power:", second**2)

    is_between = 10 <= first <= 20
    is_odd = first % 2 != 0
    print("Between 10 and 20:", is_between)
    print("Odd and in range:", is_odd and is_between)


if __name__ == "__main__":
    main()
