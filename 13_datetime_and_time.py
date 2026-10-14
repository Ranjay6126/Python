"""Practice working with date and time values."""

from datetime import datetime, timedelta


def main():
    now = datetime.now()
    print("Current date and time:", now)
    print("Formatted date:", now.strftime("%d-%m-%Y"))
    print("Formatted time:", now.strftime("%I:%M:%S %p"))

    birthday = datetime(2001, 5, 14, 9, 30)
    print("Birthday:", birthday.strftime("%A, %d %B %Y"))

    future = now + timedelta(days=7, hours=3)
    print("One week and 3 hours later:", future)

    age_days = (now - birthday).days
    print("Approximate age in days:", age_days)


if __name__ == "__main__":
    main()
