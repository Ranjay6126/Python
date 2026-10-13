"""Practice text and JSON files using a temporary practice folder."""

import json
from pathlib import Path


def main():
    practice_folder = Path("python_practice_data")
    practice_folder.mkdir(exist_ok=True)

    text_path = practice_folder / "notes.txt"
    text_path.write_text("Python practice\nKeep learning!\n", encoding="utf-8")
    print("Text file contents:")
    print(text_path.read_text(encoding="utf-8"), end="")

    data_path = practice_folder / "progress.json"
    progress = {"lesson": 10, "topics": ["loops", "functions", "files"]}
    data_path.write_text(json.dumps(progress, indent=2), encoding="utf-8")
    loaded_progress = json.loads(data_path.read_text(encoding="utf-8"))
    print("Saved progress:", loaded_progress)


if __name__ == "__main__":
    main()
