import json
from pathlib import Path

FILE_PATH = Path(__file__).resolve().parent / "habits.json"

def load_habits():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        # لازم يكون List of dicts
        if isinstance(data, list):
            return [x for x in data if isinstance(x, dict)]
        return []

    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        # إذا الملف فاضي/مخربط JSON
        return []

