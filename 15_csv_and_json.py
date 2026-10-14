"""Practice reading and writing CSV and JSON data."""

import csv
import json
from pathlib import Path


def main():
    directory = Path("python_practice_data")
    directory.mkdir(exist_ok=True)

    csv_path = directory / "students.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "course", "score"])
        writer.writerow(["Ranjay", "Python", 92])
        writer.writerow(["Asha", "JavaScript", 88])

    with csv_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("CSV data:")
        for row in reader:
            print(row)

    json_path = directory / "student_report.json"
    report = {
        "class_name": "Python Basics",
        "students": [
            {"name": "Ranjay", "score": 92},
            {"name": "Asha", "score": 88}
        ]
    }
    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("JSON data:")
    print(json_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
