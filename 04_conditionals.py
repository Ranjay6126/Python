"""Practice decisions with if, elif, and else."""


def grade_for(score):
    if not 0 <= score <= 100:
        return "Score must be between 0 and 100."
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"


def main():
    for score in (95, 82, 73, 64, 48, 105):
        print(f"Score {score}: {grade_for(score)}")


if __name__ == "__main__":
    main()
