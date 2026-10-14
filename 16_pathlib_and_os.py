"""Practice using pathlib and os to manage files and folders."""

import os
from pathlib import Path


def main():
    root = Path("python_practice_data")
    root.mkdir(exist_ok=True)

    file_path = root / "demo.txt"
    file_path.write_text("Python file system demo\nWorking with pathlib and os\n", encoding="utf-8")

    print("Current working directory:", os.getcwd())
    print("Demo file exists:", file_path.exists())
    print("File size:", file_path.stat().st_size, "bytes")
    print("File name:", file_path.name)
    print("Parent folder:", file_path.parent)

    for item in root.iterdir():
        print("Item:", item.name, "| Type:", "file" if item.is_file() else "directory")

    backup_path = root / "demo_backup.txt"
    file_path.replace(backup_path)
    print("Backup created:", backup_path.exists())


if __name__ == "__main__":
    main()
