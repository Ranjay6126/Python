"""Practice importing built-in modules and using them in scripts."""

import math
import random
import statistics


def main():
    print("Square root of 144:", math.sqrt(144))
    print("Value of pi:", math.pi)

    numbers = [10, 25, 30, 45, 50]
    print("Average:", statistics.mean(numbers))
    print("Median:", statistics.median(numbers))

    random_number = random.randint(1, 100)
    print("Random number:", random_number)

    dice_roll = random.choice([1, 2, 3, 4, 5, 6])
    print("Dice roll:", dice_roll)


if __name__ == "__main__":
    main()
