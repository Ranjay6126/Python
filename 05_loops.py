"""Practice for loops, while loops, and loop control."""


def main():
    numbers = [3, 6, 9, 12, 15]
    total = 0
    for number in numbers:
        total += number
    print("Sum:", total)

    print("Odd numbers:")
    for number in range(1, 11):
        if number % 2 == 0:
            continue
        print(number, end=" ")
    print()

    countdown = 3
    while countdown > 0:
        print("Countdown:", countdown)
        countdown -= 1
    print("Go!")


if __name__ == "__main__":
    main()
